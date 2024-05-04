const CreateIcon = ({ filled = true }) => {
  return filled ? (
    <svg
      className="icon"
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="#212121"
      viewBox="0 0 256 256"
    >
      <path d="M208,32H48A16,16,0,0,0,32,48V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V48A16,16,0,0,0,208,32ZM168,136H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32a8,8,0,0,1,0,16Z"></path>
    </svg>
  ) : (
    <svg
      className="icon"
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="#212121"
      viewBox="0 0 256 256"
    >
      <path d="M208,32H48A16,16,0,0,0,32,48V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V48A16,16,0,0,0,208,32Zm0,176H48V48H208V208Zm-32-80a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32A8,8,0,0,1,176,128Z"></path>
    </svg>
  );
};

export default CreateIcon;
