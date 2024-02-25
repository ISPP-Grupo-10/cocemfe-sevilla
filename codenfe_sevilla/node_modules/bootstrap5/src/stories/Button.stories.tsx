import React from "react";
import { Story, Meta } from "@storybook/react";

import { Button as Component } from "../";
import { ButtonProps } from "../components/Buttons/Button";

export default {
  title: "Buttons/Common",
} as Meta;

const Template: Story<ButtonProps> = (args) => <Component {...args} />;

export const Primary = Template.bind({});
Primary.args = {
  label: "Primary",
};

export const Secondary = Template.bind({});
Secondary.args = {
  label: "Secondary",
  variant: "secondary",
};

export const Success = Template.bind({});
Success.args = {
  label: "Success",
  variant: "success",
};

export const Danger = Template.bind({});
Danger.args = {
  label: "Danger",
  variant: "danger",
};

export const Warning = Template.bind({});
Warning.args = {
  label: "Warning",
  variant: "warning",
};

export const Info = Template.bind({});
Info.args = {
  label: "Info",
  variant: "info",
};

export const Light = Template.bind({});
Light.args = {
  label: "Light",
  variant: "light",
};

export const Dark = Template.bind({});
Dark.args = {
  label: "Dark",
  variant: "dark",
};

export const Link = Template.bind({});
Link.args = {
  label: "Link",
  variant: "link",
};
