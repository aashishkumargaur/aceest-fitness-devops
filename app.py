from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    # In-memory "database" for demo purposes
    app.config["MEMBERS"] = {}
    app.config["CLASSES"] = [
        {"id": 1, "name": "Yoga", "slots": 20},
        {"id": 2, "name": "HIIT", "slots": 15},
        {"id": 3, "name": "Strength Training", "slots": 10},
    ]

    @app.get("/")
    def health():
        return jsonify({"status": "ok", "service": "ACEest Fitness & Gym API"}), 200

    @app.get("/classes")
    def get_classes():
        return jsonify({"classes": app.config["CLASSES"]}), 200

    @app.post("/members")
    def add_member():
        data = request.get_json(silent=True) or {}
        required = {"member_id", "name"}
        if not required.issubset(data):
            return jsonify({"error": "member_id and name are required"}), 400
        member_id = str(data["member_id"])
        if member_id in app.config["MEMBERS"]:
            return jsonify({"error": "member already exists"}), 409
        app.config["MEMBERS"][member_id] = {"name": data["name"], "active": True}
        return jsonify({"message": "member added", "member": app.config["MEMBERS"][member_id]}), 201

    @app.get("/members/<member_id>")
    def get_member(member_id):
        m = app.config["MEMBERS"].get(str(member_id))
        if not m:
            return jsonify({"error": "not found"}), 404
        return jsonify({"member_id": member_id, **m}), 200

    return app

# For local execution: `python app.py`
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
