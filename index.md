---
layout: default
title: Home
description: "AI-powered experiential learning for students and educators. Practice decisions through simulations, quick cases, and learning games."
---

<div class="hero-flex">
  <div>
    <h1>Don't just learn the theory.<br>Experience the decision.</h1>
    <p class="lead">Interactive simulations, quick cases, and learning games designed to help students apply concepts, practice decisions, and learn from feedback.</p>
    <p class="sub">Learn by doing. Teach with confidence. Apply AI in the real world.</p>
    <div class="hero-ctas">
      <a class="btn-primary" href="{{ '/simulations/' | relative_url }}">Start Learning</a>
      <a class="btn-secondary" href="#faculty">For Faculty</a>
    </div>
  </div>
  <div class="decision-card">
    <div class="role">You are the CMO</div>
    <div class="scenario">Your new product is underperforming.</div>
    <div class="budget">₹50 lakh remaining in your marketing budget.</div>
    <div class="decision-choices">
      <button disabled>○ Increase advertising</button>
      <button disabled>○ Change positioning</button>
      <button disabled>○ Reduce price</button>
      <button disabled>○ Improve distribution</button>
    </div>
  </div>
</div>

<div class="section center">
  <div class="section-label">One Platform, Three Ways to Learn</div>
  <h2 class="section-title">Practice, don't just read.</h2>
  <div class="cards">
    <a class="card" href="{{ '/simulations/' | relative_url }}">
      <h3>Simulations</h3>
      <p>Practice real decisions before facing them in the real world. Interactive role-play scenarios in marketing, strategy, leadership, entrepreneurship, and AI adoption.</p>
    </a>
    <a class="card" href="{{ '/tools/quick-case-generator.html' | relative_url }}">
      <h3>Quick Case Generator</h3>
      <p>Turn theories and current events into classroom-ready cases. Faculty create concise, decision-oriented cases around any subject, theory, or news story.</p>
    </a>
    <div class="card" style="cursor:default;">
      <span class="badge soon">Coming Soon</span>
      <h3>Learning Games</h3>
      <p>Turn concepts into interactive classroom competitions — points, streaks, teams, and concept mastery, with immediate feedback.</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-label">The Difference</div>
  <h2 class="section-title">Learning by doing changes everything.</h2>
  <div class="flow-compare">
    <div>
      <h4>Traditional Learning</h4>
      <div class="flow old">
        <span class="flow-step">Read</span><span class="flow-arrow">→</span>
        <span class="flow-step">Memorize</span><span class="flow-arrow">→</span>
        <span class="flow-step">Exam</span>
      </div>
    </div>
    <div>
      <h4>AIjuggernauts</h4>
      <div class="flow new">
        <span class="flow-step">Learn</span><span class="flow-arrow">→</span>
        <span class="flow-step">Practice</span><span class="flow-arrow">→</span>
        <span class="flow-step">Decide</span><span class="flow-arrow">→</span>
        <span class="flow-step">Feedback</span><span class="flow-arrow">→</span>
        <span class="flow-step">Reflect</span><span class="flow-arrow">→</span>
        <span class="flow-step">Try Again</span>
      </div>
    </div>
  </div>
</div>

<div class="section center" id="try-it">
  <div class="section-label">Try It Now</div>
  <h2 class="section-title">Experience AIjuggernauts in 2 minutes.</h2>
  <p class="section-sub">Don't take our word for it. Try a decision.</p>
  <div class="decision-card" style="max-width: 480px; margin: 0 auto; text-align: left;">
    <div class="role">You are the Marketing Manager</div>
    <div class="scenario">Your company launched a new healthy snack brand. Sales are below expectations. You have ₹50 lakh remaining, and the CEO wants results within 90 days.</div>
    <div class="decision-choices" id="demo-choices">
      <button onclick="showResult('advertising')">A — Increase advertising</button>
      <button onclick="showResult('positioning')">B — Reposition the brand</button>
      <button onclick="showResult('price')">C — Reduce the price</button>
      <button onclick="showResult('distribution')">D — Expand distribution</button>
    </div>
    <div class="decision-result" id="demo-result"></div>
  </div>
</div>

<div class="section">
  <div class="section-label">For Students</div>
  <h2 class="section-title">Stop memorizing. Start practicing.</h2>
  <p class="section-sub">Build confidence by applying concepts to realistic situations. Make decisions, see consequences, receive feedback, and try again.</p>
  <div class="feature-grid">
    <div class="feature-item"><h4>Practice</h4><p>Apply classroom concepts to realistic situations.</p></div>
    <div class="feature-item"><h4>Decide</h4><p>Make decisions with incomplete information and competing priorities.</p></div>
    <div class="feature-item"><h4>Get Feedback</h4><p>Understand what you did well and what you could improve.</p></div>
    <div class="feature-item"><h4>Build Confidence</h4><p>Practice before applying your knowledge in the real world.</p></div>
  </div>
  <p style="margin-top: 26px;"><a class="btn-secondary" href="{{ '/simulations/' | relative_url }}">Explore Student Experiences →</a></p>
</div>

<div class="section" id="faculty">
  <div class="section-label">For Faculty</div>
  <h2 class="section-title">Turn your syllabus into experiences.</h2>
  <p class="section-sub">Create engaging learning activities around the concepts you already teach.</p>
  <div class="cards">
    <a class="card" href="{{ '/tools/simulation-creator.html' | relative_url }}"><h3>Create Simulations</h3><p>Build realistic role-play scenarios for your students.</p></a>
    <a class="card" href="{{ '/tools/quick-case-generator.html' | relative_url }}"><h3>Generate Quick Cases</h3><p>Turn theories and current events into classroom-ready cases.</p></a>
    <div class="card" style="cursor:default;"><span class="badge soon">Coming Soon</span><h3>Create Learning Games</h3><p>Turn concepts into interactive competitions and challenges.</p></div>
    <div class="card" style="cursor:default;"><span class="badge soon">Coming Soon</span><h3>Analyze Learning</h3><p>Understand which concepts students have mastered and where they need support.</p></div>
  </div>

  <div class="workflow-vert">
    <div class="flow-step">Your Topic</div>
    <div class="flow-arrow">↓</div>
    <div class="flow-step">Your Theory</div>
    <div class="flow-arrow">↓</div>
    <div class="flow-step">Your Teaching Objective</div>
    <div class="flow-arrow">↓</div>
    <div class="flow-step">Simulation / Case / Game</div>
    <div class="flow-arrow">↓</div>
    <div class="flow-step">Student Experience</div>
    <div class="flow-arrow">↓</div>
    <div class="flow-step">Feedback &amp; Learning Insights</div>
  </div>
  <div class="workflow-example">Example: Marketing → 4Ps → MBA → Product Launch Simulation</div>
</div>

<div class="section center">
  <div class="section-label">Subjects</div>
  <h2 class="section-title">Practice across business disciplines.</h2>
  <div class="subject-grid">
    <div class="subject-card"><h4>Marketing</h4><p>STP · 4Ps · Consumer Behaviour · Branding · Digital Marketing</p></div>
    <div class="subject-card"><h4>Strategy</h4><p>Porter's Five Forces · Blue Ocean · Competitive Strategy · Growth</p></div>
    <div class="subject-card"><h4>Entrepreneurship</h4><p>Business Models · Innovation · Startup Strategy · Venture Decisions</p></div>
    <div class="subject-card"><h4>Finance</h4><p>Investment Decisions · Valuation · Risk · Financial Strategy</p></div>
    <div class="subject-card"><h4>Operations</h4><p>Supply Chain · Capacity · Process · Quality</p></div>
    <div class="subject-card"><h4>Leadership &amp; HR</h4><p>Leadership · Change Management · Conflict · Motivation</p></div>
    <div class="subject-card"><h4>AI &amp; Digital</h4><p>AI Strategy · Digital Transformation · AI Adoption · AI Ethics</p></div>
    <div class="subject-card"><h4>Product &amp; Innovation</h4><p>Product Strategy · Product-Market Fit · Innovation · Pricing</p></div>
  </div>
</div>

<div class="section">
  <div class="section-label">Quick Case Generator</div>
  <h2 class="section-title">From today's news to tomorrow's classroom.</h2>
  <div class="flow new">
    <span class="flow-step">Current News</span><span class="flow-arrow">→</span>
    <span class="flow-step">Select Theory</span><span class="flow-arrow">→</span>
    <span class="flow-step">AIjuggernauts</span><span class="flow-arrow">→</span>
    <span class="flow-step">Quick Case</span><span class="flow-arrow">→</span>
    <span class="flow-step">Classroom Discussion</span>
  </div>
  <p style="margin-top: 26px;"><a class="btn-secondary" href="{{ '/tools/quick-case-generator.html' | relative_url }}">Generate a Quick Case →</a></p>
</div>

<div class="section">
  <div class="section-label">Resources</div>
  <h2 class="section-title">AI that matters for business and education.</h2>
  <p class="section-sub">Curated AI developments, tools, research, and ideas that matter to educators, students, and business professionals.</p>
  <p><a class="btn-secondary" href="{{ '/newsletter/' | relative_url }}">Explore AI Newsletter →</a></p>
</div>

<div class="section">
  <div class="section-label">Where Ideas Meet People</div>
  <h2 class="section-title">Upcoming conferences.</h2>
  <p class="section-sub">Discover upcoming academic and professional conferences in AI, business, management, education, and technology.</p>
  <p><a class="btn-secondary" href="{{ '/conferences/' | relative_url }}">View Conferences →</a></p>
</div>

<div class="section">
  <div class="section-label">Not Another AI Tool</div>
  <h2 class="section-title">Why AIjuggernauts?</h2>
  <table class="compare-table">
    <tr><th>Traditional Learning</th><th>AIjuggernauts</th></tr>
    <tr><td>Read</td><td>Experience</td></tr>
    <tr><td>Memorize</td><td>Apply</td></tr>
    <tr><td>Answer</td><td>Decide</td></tr>
    <tr><td>Get marks</td><td>Get feedback</td></tr>
    <tr><td>Learn once</td><td>Practice repeatedly</td></tr>
    <tr><td>Passive</td><td>Interactive</td></tr>
  </table>
</div>

<div class="section">
  <div class="section-label">What Students Build</div>
  <h2 class="section-title">Learning outcomes.</h2>
  <div class="feature-grid">
    <div class="feature-item"><h4>Decision-Making</h4><p>Make choices under uncertainty.</p></div>
    <div class="feature-item"><h4>Critical Thinking</h4><p>Evaluate alternatives and trade-offs.</p></div>
    <div class="feature-item"><h4>Application</h4><p>Apply frameworks to realistic situations.</p></div>
    <div class="feature-item"><h4>Reflection</h4><p>Understand why a decision worked or failed.</p></div>
    <div class="feature-item"><h4>AI Fluency</h4><p>Use AI thoughtfully rather than passively.</p></div>
    <div class="feature-item"><h4>Confidence</h4><p>Practice before facing real-world situations.</p></div>
  </div>
</div>

<div class="section">
  <div class="final-cta">
    <h2>Ready to learn by doing?</h2>
    <p>Explore simulations, create a case, or turn your next lesson into an interactive learning experience.</p>
    <div class="hero-ctas" style="justify-content:center;">
      <a class="btn-primary" href="{{ '/simulations/' | relative_url }}">Start Learning</a>
      <a class="btn-secondary" href="#faculty">I'm Faculty</a>
    </div>
  </div>
</div>

<script>
const outcomes = {
  advertising: {
    text: "Increased spend gets more eyes on the product, but early data suggests awareness was never the core problem — trial rates barely move.",
    concept: "Concept applied: Marketing Mix (Promotion)"
  },
  positioning: {
    text: "Your research suggests consumers understand the product, but don't see a strong reason to choose it over established brands.",
    concept: "Concept applied: Positioning"
  },
  price: {
    text: "Sales tick up short-term, but margins shrink fast and the brand starts competing on price against players who can go lower.",
    concept: "Concept applied: Pricing Strategy"
  },
  distribution: {
    text: "More shelf presence helps, but only where the target customer already shops — the underlying demand problem stays largely unsolved.",
    concept: "Concept applied: Distribution Strategy"
  }
};

function showResult(choice) {
  const outcome = outcomes[choice];
  const resultBox = document.getElementById('demo-result');
  resultBox.innerHTML = outcome.text + '<br><span class="concept-tag">' + outcome.concept + '</span><br><button class="decision-restart" onclick="resetDemo()">Try another choice</button><br><a class="btn-secondary" style="margin-top:14px; display:inline-block;" href="/simulations/">Want to experience the full simulation? &rarr;</a>';
  resultBox.style.display = 'block';
  document.getElementById('demo-choices').style.display = 'none';
}

function resetDemo() {
  document.getElementById('demo-result').style.display = 'none';
  document.getElementById('demo-choices').style.display = 'flex';
}
</script>
