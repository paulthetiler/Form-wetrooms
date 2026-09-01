import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title:
    "FORM Wetrooms | Specialist Wetroom Construction & Porcelain Installation",
  description:
    "FORM Wetrooms — specialist wetroom construction, waterproofing and precision porcelain installation across Warrington, Lymm, Knutsford, Hale and Cheshire.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
