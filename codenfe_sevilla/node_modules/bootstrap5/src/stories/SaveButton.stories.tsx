import React from "react";
import { Story, Meta } from "@storybook/react";

import { SaveButton as Component } from "../";
import { SaveButtonProps } from "../components/Buttons/SaveButton";

export default {
  title: "Buttons",
} as Meta;

export const SaveButton: Story<SaveButtonProps> = (args) => (
  <Component {...args} />
);

SaveButton.args = {
  label: "Save",
};
