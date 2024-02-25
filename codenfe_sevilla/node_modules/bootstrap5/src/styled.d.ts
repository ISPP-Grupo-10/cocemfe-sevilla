import "styled-components";
interface IPalette {
  main: string;
  contrastText: string;
}
declare module "styled-components" {
  export interface DefaultTheme {
    name: string;
    borderRadius: string;
    palette: {
      common: {
        black: string;
        white: string;
      };
      primary: IPalette;
      secondary: IPalette;
      success: IPalette;
      danger: IPalette;
      warning: IPalette;
      info: IPalette;
      light: IPalette;
      dark: IPalette;
      link: IPalette;
    };
  }
}
