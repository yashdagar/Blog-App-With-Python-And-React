from flask import request, jsonify


def isAdmin():
    username = request.json.get("username", "").strip().lower()

    if username == "":
        return jsonify({"message": "The username can not be empty"}), 400

    if username == "admin":
        return jsonify({"message": "The user is the admin"}), 200
    else:
        return jsonify({"message": "The user is not the admin"}), 400


def getUserPosts():
    with open("posts.txt") as file:
        posts = []
        for post in file.read().split("\n"):
            if post.strip() == "": continue
            values = post.split("~")
            username = values[0]
            head = values[1]
            body = values[2]
            tags = [i for i in values[3].split("^")]
            postTime = values[4]
            likes = [i for i in values[5].split("/") if i != ""]
            posts.append({
                "username": username,
                "head": head,
                "tags": tags,
                "body": body,
                "time": postTime,
                "likes": likes,
            })

        userPosts = {}
        for post in posts:
            username, head, tags, body, time, likes = post.values()
            if username not in userPosts:
                userPosts[username] = [post]
            else:
                userPosts[username].append(post)

    return jsonify({"message": "Posts loaded successfully", "posts": userPosts}), 200


def getReports():
    reports = []
    with open("reports.txt") as file:
        reports = [i for i in file.read().split("\n") if i.strip() != ""]

    posts = []
    with open("posts.txt") as file:
        for post in file.read().split("\n"):
            if post.strip() == "": continue
            if post.split("~")[4] in reports:
                values = post.split("~")
                username = values[0]
                head = values[1]
                body = values[2]
                tags = [i for i in values[3].split("^")]
                postTime = values[4]
                likes = [i for i in values[5].split("/") if i != ""]
                posts.append({
                    "username": username,
                    "head": head,
                    "tags": tags,
                    "body": body,
                    "time": postTime,
                    "likes": likes,
                })

    return jsonify({"message": "Posts loaded successfully", "posts": posts}), 200
