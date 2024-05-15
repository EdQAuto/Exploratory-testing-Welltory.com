from selene import browser, be, have


browser.open('https://app.welltory.com/auth/signin/')
browser.element('id="email"').type('ilyasoveduard@gmail.com')
browser.element('id="password"').type('Erik20041984').press_enter()
browser.open('https://app.welltory.com/user/onboarding/')
browser.element('typography_typography__KBwCq typography_h1__WK5Nc OnboardingPage_h1__FvmPQ mt-6 mb-12 cy-onboarding-title').should(have.text('Welcome to Welltory autotests'))

browser.element('id="password"').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
