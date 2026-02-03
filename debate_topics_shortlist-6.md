# Capital Markets Technology Debate Topics - Shortlist of 6

**Target Audience:** Technology professionals (developers, testers, PMs, BAs) in capital markets division of investment bank

**The Core Distinction:** Both approaches leverage AI intelligence, but differ in control paradigms:
- **Agentic AI Workflow**: Give AI a goal → Let AI determine its own path to achieve it
- **Deterministic AI Workflow**: Give AI a goal + prescribed steps → AI follows controlled path

**The Story:** Your bank is undergoing a major technology transformation. The CTO has announced that all teams must integrate AI into their workflows within 12 months. But there's a heated debate: should you give AI autonomy to find its own solutions, or maintain strict control with prescribed steps? Each team faces this choice in their daily work...

---

## 1. System Diagnostics
### The Midnight Crisis: System Failure During Critical Operations 🚨

**Target Audience:** Developers, DevOps Engineers, Support Teams

**Scenario:**  
It's 2 AM. The primary data processing system that feeds 200+ applications across the bank has crashed. Regulatory reporting deadlines loom in 6 hours. The on-call team is scrambling. Your AI-powered diagnostic system could help, but how?

**The Tension:**  
**Deterministic AI Workflow**: AI follows your carefully crafted runbooks - checking predefined failure patterns, running systematic health checks, escalating through established procedures. Predictable, auditable, but might miss the novel root cause.

**Agentic AI Workflow**: AI autonomously explores the system, correlating unusual patterns across logs, metrics, and dependencies. It might discover the real issue faster, but could also go down rabbit holes or suggest risky fixes.

**No Clear Winner:**  
When your career depends on fixing it fast, do you trust AI to follow the proven playbook, or let it think outside the box?

**Polling Question:**  
"In a critical system failure, would you rather have AI: **Follow proven diagnostic procedures** or **Autonomously explore and reason through the problem**?"

---

## 2. System Integration
### The Integration Nightmare: Connecting Legacy and Modern Systems 🔌

**Target Audience:** Integration Developers, Solution Architects, Business Analysts

**Scenario:**  
Your team must connect a 20-year-old mainframe risk system with a new cloud-based analytics platform. The mainframe team says "don't touch our code," the cloud team wants "clean APIs," and the business wants it done in 8 weeks. The data formats are incompatible, and the business rules are buried in decades of undocumented code.

**The Tension:**  
**Deterministic AI Workflow**: AI helps you build systematic data mapping rules, generates standard transformation patterns, and creates predictable integration workflows. Safe, but might miss business nuances buried in the legacy system.

**Agentic AI Workflow**: AI analyzes the actual data flows, discovers hidden business rules, and suggests creative integration patterns. Could unlock better solutions, but might create integrations that are hard to maintain or explain.

**No Clear Winner:**  
When bridging 20 years of technology evolution, do you want AI to follow integration best practices, or discover what the systems actually do?

**Polling Question:**  
"For complex legacy integration, should AI: **Apply standard integration patterns** or **Discover and adapt to actual system behaviors**?"

---

## 3. Quality Assurance
### The Testing Dilemma: Quality vs. Speed in Regulatory Environment 🧪

**Target Audience:** QA Engineers, Test Managers, Business Analysts, Product Managers

**Scenario:**  
A new regulatory requirement drops with 90 days to implement. Your team must test changes across 50+ interconnected systems. Manual testing would take 6 months. Automated testing might miss edge cases that could result in regulatory fines. The business is breathing down your neck, and regulators don't accept "we tested what we could."

**The Tension:**  
**Deterministic AI Workflow**: AI generates comprehensive test cases following regulatory compliance patterns, ensuring every requirement is systematically verified. Thorough and auditable, but might miss real-world scenarios.

**Agentic AI Workflow**: AI creates dynamic test scenarios by analyzing actual user behaviors and system interactions, potentially finding issues that standard tests miss. More realistic, but harder to prove completeness to regulators.

**No Clear Winner:**  
When regulatory compliance is non-negotiable, do you trust AI to follow the testing checklist, or to think like a regulator?

**Polling Question:**  
"For regulatory compliance testing, should AI: **Follow systematic test coverage patterns** or **Generate realistic scenario-based tests**?"

---

## 4. Release Management
### The Deployment Gamble: Zero Downtime in a 24/7 World 🚀

**Target Audience:** DevOps Engineers, Release Managers, Product Managers, Developers

**Scenario:**  
Your customer-facing trading platform serves clients across 15 time zones. There's no "maintenance window." A critical security patch must be deployed, but the last deployment caused a 3-minute outage that cost the bank $2M in SLA penalties. The business wants guarantees, but you know that no deployment is risk-free.

**The Tension:**  
**Deterministic AI Workflow**: AI manages deployments following battle-tested blue-green procedures, with predefined rollback triggers and systematic health checks. Predictable and safe, but might be overly cautious.

**Agentic AI Workflow**: AI analyzes real-time system behavior, user patterns, and market conditions to make intelligent deployment decisions. Could optimize for minimal impact, but might make choices you can't predict or explain.

**No Clear Winner:**  
When millions are at stake, do you want AI to follow the deployment playbook, or to read the room and adapt?

**Polling Question:**  
"For critical zero-downtime deployments, should AI: **Follow proven deployment procedures** or **Make intelligent real-time deployment decisions**?"

---

## 5. Performance Optimization
### The Performance Crisis: When Everything Slows Down 📈

**Target Audience:** Performance Engineers, System Architects, Developers, Operations Teams

**Scenario:**  
It's month-end reporting. Every system is under maximum load. Response times are creeping up. Users are complaining. The CEO is asking questions. You have 30 minutes before the evening news cycle picks up the story about your bank's "technical difficulties." Your monitoring shows bottlenecks everywhere, but which one do you fix first?

**The Tension:**  
**Deterministic AI Workflow**: AI applies systematic performance optimization techniques - analyzing CPU, memory, network patterns through established methodologies. Methodical and explainable, but might optimize the wrong thing first.

**Agentic AI Workflow**: AI holistically analyzes the entire system ecosystem, user behavior patterns, and business impact to prioritize optimizations. Could find the real bottleneck faster, but might make changes you don't fully understand.

**No Clear Winner:**  
When performance problems cascade, do you want AI to follow performance tuning best practices, or to see the big picture?

**Polling Question:**  
"During a performance crisis, should AI: **Apply systematic optimization techniques** or **Holistically analyze and prioritize fixes**?"

---

## 6. Code Review
### The Code Review Dilemma: Human Judgment vs. AI Intelligence 👀

**Target Audience:** Senior Developers, Tech Leads, Architects, Code Reviewers

**Scenario:**  
Your team is reviewing code for a new algorithmic trading feature. The developer who wrote it just left for another company. The code works in testing, but it's complex, handles millions in transactions, and uses machine learning models that evolve over time. You need to approve it for production, but do you really understand what it does?

**The Tension:**  
**Deterministic AI Workflow**: AI performs systematic code review - checking security patterns, performance anti-patterns, coding standards, and regulatory compliance rules. Thorough and consistent, but might miss business logic flaws.

**Agentic AI Workflow**: AI understands the business context, analyzes the algorithm's behavior, and provides insights about potential edge cases and market risks. More insightful, but less predictable in what it flags.

**No Clear Winner:**  
When approving code that handles millions, do you want AI to check the boxes, or to understand the business?

**Polling Question:**  
"For critical financial code review, should AI: **Systematically check compliance and standards** or **Analyze business logic and contextual risks**?"

---

**The Stakes:** Each choice shapes not just your current project, but your team's future relationship with AI. Choose wisely - your career, your team's success, and your bank's competitive advantage depend on it.