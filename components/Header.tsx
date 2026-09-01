import Link from "next/link";
import { FormLogo } from "./brand/FormLogo";

export function Header() {
  return (
    <header>
      <div className="wrap nav">
        <Link className="brandmark" href="/" aria-label="FORM Wetrooms home">
          <FormLogo variant="header" />
        </Link>
        <nav className="navlinks">
          <a href="#approach">Approach</a>
          <a href="#expertise">Expertise</a>
          <a href="#work">Work</a>
          <a className="top-cta" href="#contact">
            Estimate your wetroom
          </a>
        </nav>
      </div>
    </header>
  );
}
