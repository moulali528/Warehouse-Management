import {
  Box,
  Button,
  FormControl,
  FormHelperText,
  Grid,
  IconButton,
  Input,
  InputLabel,
  Modal,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import CloseIcon from "@mui/icons-material/Close";
import useUserRegister from "../hooks/useUserRegister";

interface RegisterFormProps {
  open: boolean;
  handleClose: () => void;
}

export interface FormData {
  email: string;
  username: string;
  first_name: string;
  last_name: string;
  hased_password: string;
  isActive: boolean;
  role: string;
}
const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  boxShadow: 24,
  p: 4,
  borderRadius: "16px", // Rounded corners
};

const RegisterForm: React.FC<RegisterFormProps> = ({ open, handleClose }) => {
  const { mutate, isPending, error, data: userdetails } = useUserRegister();

  const [formData, setFormData] = useState<FormData>({
    email: "",
    username: "",
    first_name: "",
    last_name: "",
    hased_password: "",
    isActive: true,
    role: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const hendelFormSubmit = () => {
    console.log("Submitting:", formData);
    mutate(formData);
    handleClose();
  };

  return (
    <>
      {userdetails && <p> User Has been Registered!</p>}
      <Modal open={open} onClose={handleClose}>
        <Box sx={style}>
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
          >
            <Typography variant="h6">Register</Typography>
            <IconButton onClick={handleClose}>
              <CloseIcon />
            </IconButton>
          </Box>
          <Box
            component="form"
            display="flex"
            flexDirection="column"
            gap={2}
            mt={2}
          >
            <TextField
              label="Email"
              name="email"
              type="email"
              fullWidth
              onChange={handleChange}
            />
            <TextField
              label="Username"
              name="username"
              fullWidth
              onChange={handleChange}
            />
            <TextField
              label="FirstName"
              name="first_name"
              fullWidth
              onChange={handleChange}
            />
            <TextField
              label="LastName"
              name="last_name"
              fullWidth
              onChange={handleChange}
            />
            <TextField
              label="Password"
              name="hased_password"
              type="password"
              fullWidth
              onChange={handleChange}
            />
            <TextField
              label="Role"
              name="role"
              type="role"
              fullWidth
              onChange={handleChange}
            />
            <Button
              variant="contained"
              color="primary"
              fullWidth
              onClick={hendelFormSubmit}
            >
              Submit
            </Button>
          </Box>
        </Box>
      </Modal>
      {isPending && <p>Submitting...</p>}
      {error && <p>Error: {error.message}</p>}
    </>
  );
};

export default RegisterForm;
