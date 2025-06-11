import { useMutation } from "@tanstack/react-query";
import { type FormData } from "../Register/RegisterForm";

const userRegister = async (useRegisterDetails: FormData) => {
  console.log("useRegisterDetails----", useRegisterDetails);

  // Ensure the request payload is correctly structured
  const formattedDetails = {
    email: useRegisterDetails.email,
    username: useRegisterDetails.username,
    first_name: useRegisterDetails.first_name,
    last_name: useRegisterDetails.last_name,
    hased_password: useRegisterDetails.hased_password, // Ensure correct field name
    role: useRegisterDetails.role,
    is_Active: useRegisterDetails.isActive,
  };
  const response = await fetch("http://localhost:8000/user/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formattedDetails),
  });

  if (!response.ok) {
    const errorMessage = await response.text(); // Capture more detailed error messages
    throw new Error(`Failed to submit user: ${errorMessage}`);
  }

  return response.json(); // Returning parsed JSON data
};

const useUserRegister = () => {
  return useMutation({
    mutationFn: (useRegisterDetails: FormData) =>
      userRegister(useRegisterDetails),
  });
};

export default useUserRegister;
