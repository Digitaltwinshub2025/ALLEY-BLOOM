// Cache Buster - Clears cache and forces fresh loads
(function() {
    'use strict';
    
    const CACHE_VERSION = 'v' + Date.now();
    const DEBUG = true;
    
    function log(message, data = null) {
        if (DEBUG) {
            const timestamp = new Date().toLocaleTimeString();
            if (data) {
                console.log(`[${timestamp}] 🔄 ${message}`, data);
            } else {
                console.log(`[${timestamp}] 🔄 ${message}`);
            }
        }
    }
    
    // Clear browser cache on page load
    function clearBrowserCache() {
        log('Clearing browser cache...');
        
        // Clear all localStorage
        try {
            localStorage.clear();
            log('✓ LocalStorage cleared');
        } catch (e) {
            log('⚠ LocalStorage clear failed:', e.message);
        }
        
        // Clear all sessionStorage
        try {
            sessionStorage.clear();
            log('✓ SessionStorage cleared');
        } catch (e) {
            log('⚠ SessionStorage clear failed:', e.message);
        }
        
        // Clear service workers
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.getRegistrations().then(registrations => {
                registrations.forEach(registration => {
                    registration.unregister();
                    log('✓ Service Worker unregistered');
                });
            }).catch(e => {
                log('⚠ Service Worker clear failed:', e.message);
            });
        }
    }
    
    // Add cache-busting query parameters to all static assets
    function bustAssetCache() {
        log('Adding cache-bust parameters to assets...');
        
        // CSS files
        document.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
            const href = link.getAttribute('href');
            if (href && !href.includes('?')) {
                link.setAttribute('href', href + '?v=' + CACHE_VERSION);
                log('✓ CSS cache-busted:', href);
            }
        });
        
        // Script files
        document.querySelectorAll('script[src]').forEach(script => {
            const src = script.getAttribute('src');
            if (src && !src.includes('?') && !src.includes('cdn')) {
                script.setAttribute('src', src + '?v=' + CACHE_VERSION);
                log('✓ JS cache-busted:', src);
            }
        });
        
        // Image files
        document.querySelectorAll('img[src]').forEach(img => {
            const src = img.getAttribute('src');
            if (src && !src.includes('?')) {
                img.setAttribute('src', src + '?v=' + CACHE_VERSION);
                log('✓ Image cache-busted:', src);
            }
        });
    }
    
    // Force page reload with cache bypass
    function forceReload() {
        log('Forcing page reload with cache bypass...');
        window.location.href = window.location.href + (window.location.href.includes('?') ? '&' : '?') + 'nocache=' + Date.now();
    }
    
    // Monitor for changes and reload if needed
    function monitorForChanges() {
        log('Monitoring for changes...');
        
        // Check for updates every 5 seconds
        setInterval(() => {
            fetch(window.location.href, {
                method: 'HEAD',
                cache: 'no-store',
                headers: {
                    'Cache-Control': 'no-cache, no-store, must-revalidate'
                }
            }).then(response => {
                const lastModified = response.headers.get('Last-Modified');
                const eTag = response.headers.get('ETag');
                
                const stored = {
                    lastModified: sessionStorage.getItem('page_last_modified'),
                    eTag: sessionStorage.getItem('page_etag')
                };
                
                if ((lastModified && lastModified !== stored.lastModified) || 
                    (eTag && eTag !== stored.eTag)) {
                    log('✓ Page changes detected - reloading...');
                    sessionStorage.setItem('page_last_modified', lastModified || '');
                    sessionStorage.setItem('page_etag', eTag || '');
                    location.reload(true);
                }
            }).catch(e => {
                log('⚠ Change detection failed:', e.message);
            });
        }, 5000);
    }
    
    // Initialize on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            log('DOM Content Loaded - Initializing cache buster...');
            clearBrowserCache();
            bustAssetCache();
            monitorForChanges();
            log('✓ Cache buster initialized');
        });
    } else {
        log('Page already loaded - Initializing cache buster...');
        clearBrowserCache();
        bustAssetCache();
        monitorForChanges();
        log('✓ Cache buster initialized');
    }
    
    // Log page info
    log('Page URL:', window.location.href);
    log('Cache Version:', CACHE_VERSION);
    log('Timestamp:', new Date().toLocaleString());
})();
