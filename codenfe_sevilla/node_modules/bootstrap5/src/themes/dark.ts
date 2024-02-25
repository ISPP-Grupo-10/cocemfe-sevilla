import { DefaultTheme } from "styled-components";
export const darkTheme: DefaultTheme = {
  name: "dark",
  borderRadius: "5px",
  palette: {
    common: {
      black: "#222831",
      white: "#ffffff",
    },
    primary: {
      main: "#063c8a",
      contrastText: "#bbd6ff",
    },
    secondary: {
      main: "#484e53",
      contrastText: "#bbd6ff",
    },
    success: {
      main: "#0d442a",
      contrastText: "#bbd6ff",
    },
    danger: {
      main: "#8f232d",
      contrastText: "#bbd6ff",
    },
    warning: {
      main: "#977305",
      contrastText: "#0c0c0c",
    },
    info: {
      main: "#076a7f",
      contrastText: "#0c0c0c",
    },
    light: {
      main: "transparent",
      contrastText: "#0c0c0c",
    },
    dark: {
      main: "#212529",
      contrastText: "#ebebeb",
    },
    link: {
      main: "transparent",
      contrastText: "#083a83",
    },
  },
};
