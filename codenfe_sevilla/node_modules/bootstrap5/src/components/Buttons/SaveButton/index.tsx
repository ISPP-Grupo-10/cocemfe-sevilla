import React from "react";
import { FaSave } from "react-icons/fa";
import { Button } from "../Button";

export interface SaveButtonProps {
  type?: "button" | "submit" | "reset" | undefined;
  label?: string;
}

export const SaveButton: React.FC<SaveButtonProps> = ({
  type = "submit",
  label = "Gravar",
  ...rest
}) => {
  return <Button icon={FaSave} label={label} type={type} {...rest} />;
};
