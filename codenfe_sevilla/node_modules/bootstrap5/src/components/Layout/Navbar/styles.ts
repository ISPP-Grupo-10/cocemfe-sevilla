import styled from "styled-components";

export const Container = styled.nav`
  display: flex;
  align-items: center;

  background-color: ${(props) => props.theme.palette.primary.contrastText};
  color: ${(props) => props.theme.palette.primary.main};
`;

export const Logo = styled.div`
  display: flex;
  padding: 0.3rem 0.5rem;
`;

export const Tools = styled.div`
  display: flex;
  align-items: center;
  gap: 0.3rem;
  margin-left: auto;
  margin-right: 0.2rem;
`;

export const Space = styled.div`
  border-left: 1px solid;
  height: 20px;
  margin: 0.3rem;
`;
