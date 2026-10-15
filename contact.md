---
layout: page
title: Contact Us
permalink: /contact/
---

Book a demo of HealthX or SkillX, or tell us about an AI project for your institution or business.

<form action="https://formsubmit.co/anujaa.gshukla@gmail.com" method="POST" class="contact-form">
  <input type="hidden" name="_subject" value="New message from AIjuggernauts contact form">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="true">
  <input type="hidden" name="_next" value="https://aijuggernauts.com/contact/?sent=true">

  <label for="name">Name</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email</label>
  <input type="email" id="email" name="email" required>

  <label for="about">Interested in</label>
  <select id="about" name="interested_in">
    <option>HealthX</option>
    <option>SkillX</option>
    <option>AI consulting</option>
    <option>Something else</option>
  </select>

  <label for="message">Message</label>
  <textarea id="message" name="message" rows="5" required></textarea>

  <button type="submit">Send Message</button>
</form>

<p style="color: var(--muted); margin-top: 24px;">Looking for the free teaching tools? They now live on <a href="https://www.aistudytools.com/tools/">AIStudyTools</a>.</p>

<script>
(function () {
  var q = new URLSearchParams(location.search), about = q.get("about"), sel = document.getElementById("about");
  if (about && sel) {
    [].forEach.call(sel.options, function (o) { if (o.text.toLowerCase() === about.toLowerCase()) sel.value = o.value; });
    var msg = document.getElementById("message");
    if (msg && !msg.value && about !== "AI consulting") msg.value = "I would like to book a demo of " + about + ".";
  }
  if (q.get("sent")) {
    var f = document.querySelector(".contact-form");
    if (f) f.insertAdjacentHTML("beforebegin", '<p style="background:var(--panel);border:1px solid var(--border);border-left:4px solid var(--accent);border-radius:12px;padding:14px 18px;">Thank you. Your message has been sent and we will get back to you shortly.</p>');
  }
})();
</script>
