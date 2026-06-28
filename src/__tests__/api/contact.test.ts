import { describe, it, expect } from "vitest";

describe("Contact form validation", () => {
  const validateEmail = (email: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  const validateRequired = (val: string) => val.trim().length > 0;

  it("accepts valid email", () => {
    expect(validateEmail("test@example.com")).toBe(true);
  });

  it("rejects invalid email", () => {
    expect(validateEmail("not-an-email")).toBe(false);
  });

  it("rejects empty required field", () => {
    expect(validateRequired("")).toBe(false);
    expect(validateRequired("  ")).toBe(false);
  });

  it("accepts non-empty required field", () => {
    expect(validateRequired("John")).toBe(true);
  });
});

describe("Rate limiting logic", () => {
  it("allows up to 3 submissions per window", () => {
    const rateLimiter = (count: number, limit: number) => count < limit;
    expect(rateLimiter(0, 3)).toBe(true);
    expect(rateLimiter(2, 3)).toBe(true);
    expect(rateLimiter(3, 3)).toBe(false);
  });
});