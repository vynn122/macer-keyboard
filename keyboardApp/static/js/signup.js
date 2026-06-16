// let usernameInput = document.getElementById('username-input-id')
// let nicknameInput = document.getElementById('nickname-input-id')
// let passwordInput = document.getElementById('password-input-id')
const getCSRFToken = () => {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
};

const handleRoute = (route) => {
  let prepRoute = "./" + route;
  window.location.href = prepRoute;
};
const handleSignup = async () => {
  let usernameInput = document.getElementById("username-input-id");
  let nicknameInput = document.getElementById("nickname-input-id");
  let passwordInput = document.getElementById("password-input-id");

  let userNameTem = usernameInput?.value.trim();
  let nickNameTem = nicknameInput?.value.trim();
  let passwordTem = passwordInput?.value.trim();

  if (!userNameTem || !nickNameTem || !passwordTem) {
    Swal.fire({
      icon: "warning",
      title: "Missing Input",
      text: "Please fill all required fields to continue.",
    });
    return;
  }

  try {
    const signUpResp = await fetch("/api/keyboardApp/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(),
      },
      body: JSON.stringify({
        username: userNameTem,
        nickname: nickNameTem,
        password: passwordTem,
      }),
    });

    const data = await signUpResp.json();
    console.log("========Signup Response Data:========", data);

    // Handle non-success responses
    if (!signUpResp.ok) {
      throw new Error(data.Error_Message || "Failed to sign up");
    }

    Swal.fire({
      icon: "success",
      title: "Sign Up Successful",
      text: data.Message || "Please go to the home page to login.",
    }).then(() => {
      handleRoute("home");
    });
  } catch (e) {
    console.error("Signup Error:", e);

    Swal.fire({
      icon: "error",
      title: "Sign Up Failed",
      text: e.message || "An unexpected error occurred.",
    });
  }
};

// const handleSignup = async () => {
//   let usernameInput = document.getElementById("username-input-id");
//   let nicknameInput = document.getElementById("nickname-input-id");
//   let passwordInput = document.getElementById("password-input-id");

//   let userNameTem = usernameInput?.value.trim();
//   let nickNameTem = nicknameInput?.value.trim();
//   let passwordTem = passwordInput?.value.trim();
//   if (!userNameTem || !nickNameTem || !passwordTem) {
//     // alert("Please fill all required field to continue");
//     Swal.fire({
//       icon: "warning",
//       title: "Missing Input",
//       text: "Please fill all required fields to continue.",
//     });
//     return;
//   }
//   try {
//     console.log(userNameTem);
//     let signUpResp = await fetch(`/api/keyboardApp/auth/signup`, {
//       method: "POST",

//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": getCSRFToken(),
//       },
//       body: JSON.stringify({
//         username: userNameTem,
//         nickname: nickNameTem,
//         password: passwordTem,
//       }),
//     });
//     if (signUpResp.ok && signUpResp.status !== 200) {
//       throw new Error("unexpected response status");
//     }
//     let data = await signUpResp.json();

//     Swal.fire({
//       icon: "success",
//       title: "Sign Up Successful",
//       //   text: data["Message"],
//       text: "Please go to the home page to login.",
//     }).then(() => {
//       handleRoute("home");
//     });
//   } catch (e) {
//     console.log(e);
//     Swal.fire({
//       icon: "error",
//       title: "Sign Up Failed",
//       text: "Failed to sign up new user: " + e,
//     });
//   }
// };
