// Handle contact form with Turnstile
export async function handleContactForm(request, env) {
    // Only handle POST requests
    if (request.method !== 'POST') {
        return new Response('Method not allowed', { status: 405 });
    }
    
    const formData = await request.formData();
    
    // Get Turnstile token
    const turnstileToken = formData.get('cf-turnstile-response');
    
    if (!turnstileToken) {
        return new Response('Please complete the security check', { 
            status: 400,
            headers: { 'Content-Type': 'text/plain' }
        });
    }
    
    // Verify Turnstile token with Cloudflare
    const verifyResponse = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            secret: env.TURNSTILE_SECRET_KEY,
            response: turnstileToken,
            remoteip: request.headers.get('CF-Connecting-IP'),
        }),
    });
    
    const outcome = await verifyResponse.json();
    
    if (!outcome.success) {
        return new Response('Security verification failed. Please try again.', { 
            status: 400,
            headers: { 'Content-Type': 'text/plain' }
        });
    }
    
    // Remove Turnstile token before forwarding to Formspree
    const cleanFormData = new FormData();
    for (const [key, value] of formData.entries()) {
        if (key !== 'cf-turnstile-response') {
            cleanFormData.append(key, value);
        }
    }
    
    // Forward to Formspree
    const formspreeResponse = await fetch('https://formspree.io/f/xeokyqjr', {
        method: 'POST',
        body: cleanFormData,
        headers: {
            'Accept': 'application/json',
        },
    });
    
    if (formspreeResponse.ok) {
        // Redirect to thank you page
        return Response.redirect(new URL('/thank-you.html', request.url).toString(), 302);
    } else {
        return new Response('Error submitting form. Please try again later.', { 
            status: 500,
            headers: { 'Content-Type': 'text/plain' }
        });
    }
}

// Inject Turnstile site key into HTML
export async function injectTurnstileKey(response, env) {
    if (!env.TURNSTILE_SITE_KEY) {
        console.error('TURNSTILE_SITE_KEY not configured');
        return response;
    }
    
    const text = await response.text();
    const modifiedHtml = text.replace(
        'TURNSTILE_SITE_KEY_PLACEHOLDER',
        env.TURNSTILE_SITE_KEY
    );
    
    return new Response(modifiedHtml, {
        status: response.status,
        statusText: response.statusText,
        headers: response.headers
    });
}
