import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "600", "700", "800", "900"],
  variable: "--font-inter",
});

const BASE_URL = "https://veda-advisors.vercel.app";
const OG_IMAGE = `${BASE_URL}/images/MAIN%20-%20Full%20Logo%20Veda%20full%20logo%20with%20Slate%20Teak%20BG.png`;

export const metadata: Metadata = {
  metadataBase: new URL(BASE_URL),
  title: {
    default: "Veda Advisors — Stop Chasing Investors. Make Them Chase You.",
    template: "%s | Veda Advisors",
  },
  description:
    "Rajat Sir (Rajat Rajkamal Agarwal) is a Startup Fundraising Advisor with 28 years of experience. BSCVI 3.0 — a proven 5-stage system. 400+ startups funded. Stage 0 is free.",
  keywords: [
    "startup fundraising advisor",
    "startup funding India",
    "how to raise funds startup",
    "investor pitch",
    "BSCVI",
    "Rajat Sir",
    "Rajat Rajkamal Agarwal",
    "Veda Advisors",
    "startup advisor India",
    "seed funding",
    "angel investor",
  ],
  authors: [{ name: "Rajat Rajkamal Agarwal" }],
  creator: "Rajat Rajkamal Agarwal",
  publisher: "Veda Advisors",
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true },
  },
  icons: {
    icon: "/images/MAIN%20-%20Short%20Logo%20Veda%20logo%20Slate%20Teak%20BG.png",
    apple: "/images/MAIN%20-%20Short%20Logo%20Veda%20logo%20Slate%20Teak%20BG.png",
  },
  manifest: "/manifest.json",
  openGraph: {
    type: "website",
    siteName: "Veda Advisors",
    title: "Stop Chasing Investors. Make Them Chase You. | Veda Advisors",
    description:
      "Rajat Sir has helped 400+ startups raise funds using BSCVI 3.0 — a proven 5-stage advisory system. Stage 0 is free.",
    url: BASE_URL,
    images: [{ url: OG_IMAGE, width: 1200, height: 630, alt: "Veda Advisors — Startup Fundraising Advisor" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Stop Chasing Investors. Make Them Chase You.",
    description: "Rajat Sir has helped 400+ startups raise funds. Stage 0 Free Assessment.",
    images: [OG_IMAGE],
  },
  alternates: {
    canonical: BASE_URL,
  },
};

export const viewport: Viewport = {
  themeColor: "#0D2B1F",
  colorScheme: "dark",
};

/**
 * Structured data for Rajat Rajkamal Agarwal (Rajat Sir) — the principal
 * advisor behind Veda Advisors. Helps Google rich results surface him as
 * a Person entity associated with the brand.
 */
const personJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'Person',
  name: 'Rajat Rajkamal Agarwal',
  alternateName: 'Rajat Sir',
  jobTitle: 'Startup Fundraising Advisor',
  worksFor: {
    '@type': 'Organization',
    name: 'Veda Advisors',
    url: 'https://veda-advisors.vercel.app',
  },
  url: 'https://veda-advisors.vercel.app',
  image: 'https://veda-advisors.vercel.app/images/Image%201%20-%20Rajat.jpg',
  email: 'mailto:rajatkamalagarwal@gmail.com',
  description:
    'Startup fundraising advisor with 28 years of experience. Has helped 400+ startups raise funds and mentored 600+ founders. TEDx speaker.',
  knowsAbout: [
    'Startup Fundraising',
    'Angel Investment',
    'Venture Capital',
    'Term Sheets',
    'Investor Pitching',
    'BSCVI 3.0',
  ],
} as const;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.variable} style={{ margin: 0, padding: 0 }}>
        {/* schema.org JSON-LD for Rajat Sir — safe to inject via dangerouslySetInnerHTML */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(personJsonLd) }}
        />
        {children}
      </body>
    </html>
  );
}
