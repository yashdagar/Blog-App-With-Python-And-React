import "./Post.css";

import { useState } from "react";
import { useEffect } from "react";
import Tag from "../tag/Tag";
import MenuIcon from "../../icons/menu";
import LikeIcon from "../../icons/like";

const Post = ({
  curUser,
  username,
  head,
  body,
  likes,
  tags,
  time,
  handleEdit,
  handleDelete,
}) => {
  const [isLiked, setIsLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(0);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    setLikeCount(likes.length);
    likes.forEach((like) => {
      if (like === curUser) {
        setIsLiked(true);
        setLikeCount(likes.length - 1);
      }
    });
  }, [likes, curUser]);

  const handleLike = () => {
    setIsLiked(!isLiked);
    fetch("http://127.0.0.1:5000/set_like", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: curUser,
        postID: time,
      }),
    });
  };

  const handleReport = () => {
    fetch("http://localhost:5000/report", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        time: time,
      }),
    }).then((res) => res.json().then((j) => showSnackbar(j.message)));
  };

  const showSnackbar = (message) => {
    var snackbar = document.createElement("div");
    snackbar.className = "snackbar";
    snackbar.textContent = message;

    document.body.appendChild(snackbar);

    setTimeout(() => {
      snackbar.classList.add("show");
    }, 10);

    setTimeout(() => {
      snackbar.classList.remove("show");
      setTimeout(() => {
        document.body.removeChild(snackbar);
      }, 500);
    }, 3000);
  };

  return (
    <div className="postContainer">
      <div className="postHeader">
        <div
          dangerouslySetInnerHTML={{ __html: head }}
          className="postHead cormorant-garamond-bold"
        />
        <div>
          <MenuIcon onClick={() => setIsMenuOpen(!isMenuOpen)} />
          {isMenuOpen && (
            <div
              className="dropdownContainer"
              onClick={() => setIsMenuOpen(false)}
            >
              {curUser === username && (
                <>
                  <div className="dropdownItem first" onClick={handleEdit}>
                    Edit
                  </div>
                  <div className="dropdownItem" onClick={handleDelete}>
                    Delete
                  </div>
                </>
              )}
              <div className="dropdownItem last" onClick={handleReport}>
                Report
              </div>
            </div>
          )}
        </div>
      </div>
      <div className="postAuthor">Author: {username}</div>
      <p
        dangerouslySetInnerHTML={{ __html: body }}
        className="postBody cormorant-upright-regular"
      />
      <div className="postFooter">
        <div className="postTags">
          {tags.map((tag) => (
            <Tag name={tag} key={tag} />
          ))}
        </div>
        <div style={{ display: "flex", alignItems: "center" }}>
          <LikeIcon onClick={handleLike} filled={isLiked} />
          {likeCount + (isLiked ? 1 : 0)}
        </div>
      </div>
    </div>
  );
};

export default Post;
