import React, { createContext, useContext, useState } from "react";

import { DefaultTheme, ThemeProvider as Theme } from "styled-components";
import { darkTheme } from "../themes/dark";
import { lightTheme } from "../themes/light";

type ThemeContextData = {
  theme: DefaultTheme;
  setTheme: (t: DefaultTheme) => void;
};

const ThemeContext = createContext<ThemeContextData>({} as ThemeContextData);

const ThemeProvider: React.FC = ({ children }) => {
  const [theme, setTheme] = useState<DefaultTheme>(() => {
    const storedTheme = localStorage.getItem("@theme");
    return storedTheme === "dark" ? darkTheme : lightTheme;
  });

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Theme theme={theme}>{children}</Theme>
    </ThemeContext.Provider>
  );
};

function useTheme(): ThemeContextData {
  const context = useContext(ThemeContext);

  if (!context) {
    throw new Error("useTheme must be used within an ThemeProvider");
  }

  return context;
}

export { ThemeProvider, useTheme };
