const icons = {
    medals: {
        gold: `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" fill="url(#gold-gradient)" stroke="#FBBF24" stroke-width="1.5"/>
                <text x="12" y="16" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#A16207" text-anchor="middle">1</text>
                <defs>
                    <linearGradient id="gold-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:#FDE047;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#F59E0B;stop-opacity:1" />
                    </linearGradient>
                </defs>
            </svg>
        `,
        silver: `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" fill="url(#silver-gradient)" stroke="#9CA3AF" stroke-width="1.5"/>
                <text x="12" y="16" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#4B5563" text-anchor="middle">2</text>
                <defs>
                    <linearGradient id="silver-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:#E5E7EB;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#D1D5DB;stop-opacity:1" />
                    </linearGradient>
                </defs>
            </svg>
        `,
        bronze: `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" fill="url(#bronze-gradient)" stroke="#A16207" stroke-width="1.5"/>
                <text x="12" y="16" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#713F12" text-anchor="middle">3</text>
                <defs>
                    <linearGradient id="bronze-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:#FCD34D;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#D97706;stop-opacity:1" />
                    </linearGradient>
                </defs>
            </svg>
        `
    },
    styles: {
        freestyle: `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-wind">
                <path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>
            </svg>
        `,
        backstroke: `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
            </svg>
        `,
        breaststroke: `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
            </svg>
        `,
        butterfly: `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-feather">
                <path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/>
            </svg>
        `,
        medley: `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
            </svg>
        `
    },
    age: {
        new: `<span class="record-age-badge new" title="Recent record (last 2 years)">New</span>`,
        recent: `<span class="record-age-badge recent" title="Recent record (last 5 years)">Recent</span>`,
        aging: `<span class="record-age-badge aging" title="Aging record (5-10 years)">Aging</span>`,
        old: `<span class="record-age-badge old" title="Old record (10+ years)">Old</span>`
    }
};
