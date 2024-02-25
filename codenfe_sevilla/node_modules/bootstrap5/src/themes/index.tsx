import React from "react";
import { ThemeProvider as Theme } from "../hooks/theme";

export const ThemeProvider: React.FC = ({ children }) => {
  return <Theme>{children}</Theme>;
};
