type FormLogoProps = {
  variant: "hero" | "header";
};

export function FormLogo({ variant }: FormLogoProps) {
  const isHero = variant === "hero";
  const src = isHero ? "/form-logo.svg" : "/form-logo-header.svg";
  const alt = isHero
    ? "FORM Wetrooms — Designed. Engineered. Tiled."
    : "FORM Wetrooms";

  return (
    <div className="form-logo">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={src} alt={alt} />
    </div>
  );
}
