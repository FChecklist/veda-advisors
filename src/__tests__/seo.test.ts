import { describe, it, expect } from "vitest";

describe("SEO utilities", () => {
  const buildTitle = (pageTitle: string, siteName = "Veda Advisors") =>
    `${pageTitle} | ${siteName}`;

  const buildCanonical = (path: string, baseUrl = "https://vedaadvisors.com") =>
    `${baseUrl}${path}`;

  it("builds page title correctly", () => {
    expect(buildTitle("About Us")).toBe("About Us | Veda Advisors");
  });

  it("builds canonical URL correctly", () => {
    expect(buildCanonical("/about")).toBe("https://vedaadvisors.com/about");
  });

  it("homepage canonical has no trailing slash issue", () => {
    expect(buildCanonical("/")).toBe("https://vedaadvisors.com/");
  });
});