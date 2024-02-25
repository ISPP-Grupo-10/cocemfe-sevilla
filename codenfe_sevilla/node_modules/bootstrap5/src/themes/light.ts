import { DefaultTheme } from "styled-components";
export const lightTheme: DefaultTheme = {
  name: "light",
  borderRadius: "5px",
  palette: {
    common: {
      black: "#222831",
      white: "#f7f7f7",
    },
    primary: {
      main: "#0d6efd",
      contrastText: "#f7f7f7",
    },
    secondary: {
      main: "#6c757d",
      contrastText: "#f7f7f7",
    },
    success: {
      main: "#198754",
      contrastText: "#f7f7f7",
    },
    danger: {
      main: "#dc3545",
      contrastText: "#f7f7f7",
    },
    warning: {
      main: "#ffc107",
      contrastText: "#222831",
    },
    info: {
      main: "#0dcaf0",
      contrastText: "#222831",
    },
    light: {
      main: "transparent",
      contrastText: "#222831",
    },
    dark: {
      main: "#212529",
      contrastText: "#ebebeb",
    },
    link: {
      main: "transparent",
      contrastText: "#0d6efd",
    },
  },
};
