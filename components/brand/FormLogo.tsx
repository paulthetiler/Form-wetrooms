type FormLogoProps = {
  variant: "hero" | "header";
};

export function FormLogo({ variant }: FormLogoProps) {
  const isHero = variant === "hero";

  return (
    <div
      className={`form-logo form-logo--${variant}`}
      role="img"
      aria-label="FORM — Bathrooms, Wetrooms and Bespoke Tiling"
    >
      <div className="form-logo__frame" aria-hidden="true">
        <span className="form-logo__word">FORM</span>
      </div>
      <div className="form-logo__services" aria-hidden="true">
        Bathrooms <span>·</span> Wetrooms <span>·</span> Bespoke Tiling
      </div>
      {isHero ? (
        <div className="form-logo__strap" aria-hidden="true">
          Designed. Engineered. Tiled.
        </div>
      ) : null}
    </div>
  );
}
