const input = document.querySelector("input");
const button = document.querySelector("#passgen");
function GeneratePassword(length = 8) {
const randomPassword =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$!%^&*()_+=-";

  let password = "";
  for (let i = 0; i < length; ++i) {
    let at = Math.floor(Math.random() * (randomPassword.length + 1));
    password += randomPassword.charAt(at);
  }
  return password;
}
button.addEventListener("click", () => {
  input.value = GeneratePassword(8);
});