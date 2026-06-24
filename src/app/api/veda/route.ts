import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
  // Read the generated Veda Advisors index.html
  const filePath = path.join(process.cwd(), 'VedaAdvisors_Demo', 'index.html');
  const html = fs.readFileSync(filePath, 'utf-8');
  
  return new NextResponse(html, {
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
    },
  });
}