from flask import request, jsonify
import re


def registerUser():
    username = request.json.get("username", "").lower().strip()
    email = request.json.get("email", "").lower().strip()
    password = request.json.get("password", "")

    if email == "" or password == "" or username == "":
        return jsonify({"message": "Username, Email and password can not be empty"}), 400

    elif len(password) < 8:
        return jsonify({"message": "The password should be at least 8 characters"}), 400

    usernameRegex = "^[a-zA-Z0-9._]+$"
    if not re.match(usernameRegex, username):
        return jsonify({"message": "The user can only contain alphanumeric values, _ ."}), 400

    emailRegex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(emailRegex, email):
        return jsonify({"message": "Please enter a valid email"}), 400

    with open("login.txt") as file:
        for line in file.read().split("\n"):
            if line.strip() == "": continue

            oldEmail, oldPassword, oldUsername = line.split(" ")
            if oldEmail == email:
                return jsonify({"message": "User already exists"}), 409

            elif oldUsername == username:
                return jsonify({"message": "Username is taken"}), 409
    with open("login.txt", "a") as file:
        file.write(email + " " + password + " " + username + "\n")
    return jsonify({"message": "Sign in successful"}), 201


def loginUser():
    email = request.json.get("email", "")
    password = request.json.get("password", "")

    if email == "" or password == "":
        return jsonify({"message": "Email and password can not be empty"}), 400

    combinations = []
    with open("login.txt") as file:
        combinations = [(i.split(" ")[0], i.split(" ")[1], i.split(" ")[2])
                        for i in file.read().split("\n") if i.strip() != ""]

    emailRegex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(emailRegex, email):
        for e, p, u in combinations:
            if email == u and password == p:
                return jsonify({"message": "Sign in successful", "username": u}), 200
        return jsonify({"message": "Username and password do not match"}), 401

    for e, p, u in combinations:
        if email == e and password == p:
            return jsonify({"message": "Sign in successful", "username": u}), 200
    return jsonify({"message": "Email and password do not match"}), 401
