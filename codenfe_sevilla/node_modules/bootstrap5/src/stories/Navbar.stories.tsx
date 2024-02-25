import React from "react";
import { Story, Meta } from "@storybook/react";

import { Navbar as Component } from "../";
import { NavbarProps } from "../components/Layout/Navbar";

export default {
  title: "Layout",
} as Meta;

export const Navbar: Story<NavbarProps> = (args) => <Component {...args} />;
Navbar.args = {
  logo: "React Bootstrap5",
};
