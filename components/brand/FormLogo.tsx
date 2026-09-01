import { WaterDrop } from "./WaterDrop";

type FormLogoProps = {
  variant: "hero" | "header";
};

export function FormLogo({ variant }: FormLogoProps) {
  const isHero = variant === "hero";
  const src = isHero ? "/form-logo.svg" : "/form-logo-header.svg";
  const viewBox = isHero ? "0 0 1400 640" : "0 0 1400 500";
  const alt = isHero
    ? "FORM Wetrooms — Designed. Engineered. Tiled."
    : "FORM Wetrooms";

  return (
    <div className="form-logo">
      {/* SVG wordmarks keep <img> so the static mark and the React drop overlay share one box. */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={src} alt={alt} />
      <svg
        className="form-logo-drop"
        viewBox={viewBox}
        aria-hidden="true"
        focusable="false"
      >
        <WaterDrop idPrefix={variant} yOffset={isHero ? 0 : -80} />
      </svg>
    </div>
  );
}
