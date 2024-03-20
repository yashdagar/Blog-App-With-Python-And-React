from flask import request, jsonify

import time


def getPosts():
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
    return jsonify({"message": "Posts loaded successfully", "posts": posts}), 200


def addPost():
    head = request.json.get("head", "")
    body = request.json.get("body", "").replace("\n", "")
    tags = request.json.get("tags", "")
    username = request.json.get("username", "")

    if head == "" or body == "" or tags == [] or username == "":
        return jsonify({"message": "Posts should have a head, body and at least one tag"}), 400

    with open("posts.txt", "a") as file:
        file.write("~".join([username, head, body, "^".join(tags), str(int(time.time() * 1000))]) + "~\n")
    return jsonify({"message": "Post added"}), 201


def setLike():
    postID = request.json.get("postID", "")
    username = request.json.get("username", "")
    posts = []
    with open("posts.txt") as file:
        posts = file.read().split("\n")
        for i, post in enumerate(posts):
            if post.strip() == "": continue
            if post.split("~")[4] == postID:
                postData = posts[i].split("~")
                likes = postData[5].split("/")
                if username in likes:
                    likes.remove(username)
                else:
                    likes.append(username)
                postData[5] = "/".join(likes)
                posts[i] = "~".join(postData)
    with open("posts.txt", "w") as file:
        file.write("\n".join(posts))

    return jsonify({"message": "Post liked"}), 201


def reportPost():
    postID = request.json.get("time", "")

    with open("reports.txt", "a") as file:
        file.write(postID + "\n")

    return jsonify({"message": "Post reported"}), 201


def deletePost():
    postID = request.json.get("time", "")

    reports = []
    with open("reports.txt") as file:
        reports = [i for i in file.read().split("\n") if i != ""]
        if postID in reports:
            reports.remove(postID)

    with open("reports.txt", "w") as file:
        file.write("\n".join(reports) + "\n")

    posts = []
    with open("posts.txt") as file:
        posts = file.read().split("\n")
        lenBefore = len(posts)
        for i, post in enumerate(posts):
            if post.strip() == "": continue
            if post.split("~")[4] == postID:
                posts.remove(post)
                break
        if len(posts) == lenBefore:
            return jsonify({"message": "Post not found"}), 400

    with open("posts.txt", "w") as file:
        file.write("\n".join(posts) + "\n")
        return jsonify({"message": "Post deleted"}), 200


def updatePost():
    postID = request.json.get("time", "")
    head = request.json.get("head", "")
    body = request.json.get("body", "")
    tags = request.json.get("tags", "")

    posts = []
    with open("posts.txt") as file:
        posts = file.read().split("\n")
        for i, post in enumerate(posts):
            if post.strip() == "": continue
            if post.split("~")[4] == postID:
                postData = post.split("~")
                postData[1] = head
                postData[2] = body
                postData[3] = "^".join(tags)
                postData[4] = str(int(time.time() * 1000))
                posts[i] = "~".join(postData)

    with open("posts.txt", "w") as file:
        file.write("\n".join(posts))
        return jsonify({"message": "Post updated"}), 200
