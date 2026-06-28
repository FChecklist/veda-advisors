import { test, expect } from "@playwright/test";

test.describe("Homepage", () => {
  test("loads successfully", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/Veda/i);
  });

  test("has main CTA button", async ({ page }) => {
    await page.goto("/");
    const cta = page.locator("a[href*='consultation'], button:has-text('Consultation'), a:has-text('Book')").first();
    await expect(cta).toBeVisible();
  });
});

test.describe("India page", () => {
  test("loads /india", async ({ page }) => {
    const response = await page.goto("/india");
    expect(response?.status()).toBeLessThan(400);
  });
});

test.describe("SEO", () => {
  test("homepage has meta description", async ({ page }) => {
    await page.goto("/");
    const metaDesc = await page.locator('meta[name="description"]').getAttribute("content");
    expect(metaDesc).toBeTruthy();
    expect(metaDesc!.length).toBeGreaterThan(10);
  });
});