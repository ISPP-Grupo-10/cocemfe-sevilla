import React, { ButtonHTMLAttributes } from "react";
import { IconBaseProps } from "react-icons/lib";
import { Container } from "./styles";

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  type?: "button" | "submit" | "reset" | undefined;
  label?: string;
  variant?:
    | "primary"
    | "secondary"
    | "success"
    | "danger"
    | "warning"
    | "info"
    | "light"
    | "dark"
    | "link";
  icon?: React.ComponentType<IconBaseProps>;
}

export const Button: React.FC<ButtonProps> = ({
  type = "button",
  label,
  variant = "primary",
  icon: Icon,
  ...rest
}) => {
  return (
    <Container label={!!label} variant={variant} className="btn" type={type} {...rest}>
      {Icon && <Icon />}
      {label}
    </Container>
  );
};
