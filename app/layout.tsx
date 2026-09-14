import type { Metadata } from "next";
import "./globals.css";
import "./brand.css";

export const metadata: Metadata = {
  title: "FORM | Bathrooms, Wetrooms & Bespoke Tiling in Cheshire",
  description:
    "FORM creates bespoke bathrooms, engineered wetrooms and precision porcelain installations across Warrington, Lymm, Knutsford, Hale and Cheshire.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
