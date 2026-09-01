const DROP_PATH =
  "M 535.78,159.44 C 524.10,192.00 462.82,243.16 462.82,303.63 C 462.82,368.74 494.92,392.00 535.78,392.00 C 576.63,392.00 608.74,368.74 608.74,303.63 C 608.74,243.16 547.45,192.00 535.78,159.44 Z";

const HIGHLIGHT_PATH =
  "M 518.27,247.81 C 499.30,255.35 506.88,277.12 518.27,289.67 C 527.37,268.74 525.85,252.84 518.27,247.81 Z";

type WaterDropProps = {
  idPrefix: string;
  yOffset?: number;
};

export function WaterDrop({ idPrefix, yOffset = 0 }: WaterDropProps) {
  const fillId = `${idPrefix}-water-fill`;
  const sheenId = `${idPrefix}-water-sheen`;
  const shimmerId = `${idPrefix}-water-shimmer`;
  const clipId = `${idPrefix}-water-clip`;

  return (
    <g
      className="water-drop"
      transform={yOffset ? `translate(0 ${yOffset})` : undefined}
    >
      <defs>
        <linearGradient id={fillId} x1="0.28" y1="0.02" x2="0.84" y2="1">
          <stop offset="0%" stopColor="#d8f6ff" />
          <stop offset="18%" stopColor="#7ad2f2" />
          <stop offset="46%" stopColor="#2b9fd8" />
          <stop offset="74%" stopColor="#0e6eae" />
          <stop offset="100%" stopColor="#063d6a" />
        </linearGradient>
        <radialGradient id={sheenId} cx="0.38" cy="0.28" r="0.62">
          <stop offset="0%" stopColor="#ffffff" stopOpacity="0.55" />
          <stop offset="42%" stopColor="#8fd9f5" stopOpacity="0.14" />
          <stop offset="100%" stopColor="#042c4d" stopOpacity="0" />
        </radialGradient>
        <linearGradient id={shimmerId} x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stopColor="#fff" stopOpacity="0" />
          <stop offset="42%" stopColor="#fff" stopOpacity="0" />
          <stop offset="50%" stopColor="#fff" stopOpacity="0.92" />
          <stop offset="58%" stopColor="#bfefff" stopOpacity="0.28" />
          <stop offset="100%" stopColor="#fff" stopOpacity="0" />
        </linearGradient>
        <clipPath id={clipId}>
          <path d={DROP_PATH} />
        </clipPath>
      </defs>
      <path fill={`url(#${fillId})`} d={DROP_PATH} />
      <path fill={`url(#${sheenId})`} d={DROP_PATH} />
      <g clipPath={`url(#${clipId})`}>
        <rect
          className="water-drop-shimmer"
          x="430"
          y="150"
          width="58"
          height="260"
          fill={`url(#${shimmerId})`}
        />
      </g>
      <path fill="#f3fbff" opacity="0.9" d={HIGHLIGHT_PATH} />
      <ellipse
        cx="548"
        cy="210"
        rx="9"
        ry="16"
        fill="#ffffff"
        opacity="0.38"
        transform="rotate(-18 548 210)"
      />
    </g>
  );
}
