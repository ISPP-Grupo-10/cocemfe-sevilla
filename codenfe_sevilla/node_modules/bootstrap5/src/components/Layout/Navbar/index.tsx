import React from "react";
import { useCallback } from "react";
import { FaSignOutAlt, FaSun } from "react-icons/fa";
import { Button } from "../../..";
import { useTheme } from "../../../hooks/theme";
import { darkTheme } from "../../../themes/dark";
import { lightTheme } from "../../../themes/light";
import { Container, Logo, Space, Tools } from "./styles";

export type NavbarProps = {
  logo: React.ReactNode;
  signOut: () =>void;
};

export const Navbar: React.FC<NavbarProps> = ({ logo, signOut }) => {
  const { theme, setTheme } = useTheme();
  const changeTheme = useCallback(() => {
    if (theme === lightTheme) {
      setTheme(darkTheme);
      localStorage.setItem("@theme", "dark");
    } else {
      setTheme(lightTheme);
      localStorage.setItem("@theme", "light");
    }
  }, [theme, setTheme]);
  return (
    <Container>
      <Logo>{logo}</Logo>
      <Tools>
        <Button variant="link" type="button" label="" icon={FaSun} onClick={changeTheme} />
        <Space />
        <Button variant="danger" type="button" label="" icon={FaSignOutAlt} onClick={signOut} />
      </Tools>
    </Container>
  );
};
