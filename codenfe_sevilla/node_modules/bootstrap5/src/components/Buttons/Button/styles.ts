import styled, { css } from "styled-components";

type Props = {
  variant?: string;
  label: boolean;
};

export const Container = styled.button<Props>`
  display: flex;
  align-items: center;
  font-size: 1rem;
  border-radius: ${(props) => props.theme.borderRadius};

  ${props => props.label && css`
    svg {
      margin-right: 0.3rem;
    }
  `}

  :hover {
    filter: brightness(0.8);
  }

  ${(props) =>
    props.variant === "primary" &&
    css`
      background-color: ${(props) => props.theme.palette.primary.main};
      color: ${(props) => props.theme.palette.primary.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.primary.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "secondary" &&
    css`
      background-color: ${(props) => props.theme.palette.secondary.main};
      color: ${(props) => props.theme.palette.secondary.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.secondary.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "success" &&
    css`
      background-color: ${(props) => props.theme.palette.success.main};
      color: ${(props) => props.theme.palette.success.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.success.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "danger" &&
    css`
      background-color: ${(props) => props.theme.palette.danger.main};
      color: ${(props) => props.theme.palette.danger.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.danger.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "warning" &&
    css`
      background-color: ${(props) => props.theme.palette.warning.main};
      color: ${(props) => props.theme.palette.warning.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.warning.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "info" &&
    css`
      background-color: ${(props) => props.theme.palette.info.main};
      color: ${(props) => props.theme.palette.info.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.info.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "light" &&
    css`
      background-color: ${(props) => props.theme.palette.light.main};
      color: ${(props) => props.theme.palette.light.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.light.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "dark" &&
    css`
      background-color: ${(props) => props.theme.palette.dark.main};
      color: ${(props) => props.theme.palette.dark.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.dark.contrastText};
      }
    `}

  ${(props) =>
    props.variant === "link" &&
    css`
      background-color: ${(props) => props.theme.palette.link.main};
      color: ${(props) => props.theme.palette.link.contrastText};

      :hover {
        color: ${(props) => props.theme.palette.link.contrastText};
      }
    `}
`;
