"""
Preloaded Projects for Hackathon Demos.
Contains manually crafted, high-quality projects that override standard AI generation.
"""

def get_preloaded_project(schema: str) -> dict:
    """Return a preloaded project based on the schema/keyword."""
    
    if "calculator" in schema.lower() or "calc" in schema.lower():
        return {
            "project_name": "quantum-calc",
            "description": "A premium, high-performance calculator with glassmorphism UI.",
            "tech_stack": ["HTML", "CSS", "JavaScript"],
            "phases": [
                {"name": "Phase 1: Core", "tasks": ["Initialize Engine", "Setup UI"]},
                {"name": "Phase 2: Polish", "tasks": ["Add Animations", "Expert Review"]},
            ],
            "files": [
                {"path": "index.html", "description": "Layout & Structure", "language": "HTML"},
                {"path": "styles.css", "description": "Premium Styling", "language": "CSS"},
                {"path": "main.js", "description": "Calculation Logic", "language": "JavaScript"},
            ],
            "code_files": ["index.html", "styles.css", "main.js"],
            "all_code": {
                "index.html": CALCULATOR_HTML,
                "styles.css": CALCULATOR_CSS,
                "main.js": CALCULATOR_JS
            },
            "final_code": "...", # Computed later if needed
            "compliance": "PERFECT"
        }
    return None

# ==========================================
# FILE CONTENTS
# ==========================================

CALCULATOR_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quantum Calculator</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="background-globes">
        <div class="globe g1"></div>
        <div class="globe g2"></div>
        <div class="globe g3"></div>
    </div>

    <div class="calculator-container">
        <div class="display-container">
            <div class="history" id="history"></div>
            <div class="result" id="result">0</div>
        </div>
        
        <div class="keypad">
            <button class="btn func" data-action="AC">AC</button>
            <button class="btn func" data-action="+/-">+/-</button>
            <button class="btn func" data-action="%">%</button>
            <button class="btn op" data-action="/">÷</button>
            
            <button class="btn num" data-num="7">7</button>
            <button class="btn num" data-num="8">8</button>
            <button class="btn num" data-num="9">9</button>
            <button class="btn op" data-action="*">×</button>
            
            <button class="btn num" data-num="4">4</button>
            <button class="btn num" data-num="5">5</button>
            <button class="btn num" data-num="6">6</button>
            <button class="btn op" data-action="-">−</button>
            
            <button class="btn num" data-num="1">1</button>
            <button class="btn num" data-num="2">2</button>
            <button class="btn num" data-num="3">3</button>
            <button class="btn op" data-action="+">+</button>
            
            <button class="btn num zero" data-num="0">0</button>
            <button class="btn num" data-action=".">.</button>
            <button class="btn equal" data-action="=">=</button>
        </div>
    </div>
    
    <script src="main.js"></script>
</body>
</html>"""

CALCULATOR_CSS = """/* Premium Dark Theme with Glassmorphism */
:root {
    --bg-color: #050505;
    --glass-bg: rgba(20, 20, 20, 0.6);
    --glass-border: rgba(255, 255, 255, 0.08);
    --text-primary: #ffffff;
    --text-secondary: #a3a3a3;
    --accent: #8b5cf6; /* Violet */
    --accent-glow: rgba(139, 92, 246, 0.4);
    --btn-bg: rgba(255, 255, 255, 0.03);
    --btn-hover: rgba(255, 255, 255, 0.08);
    --op-color: #ff9f1c; /* Orange for operators */
    --op-hover: #ffb74d;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Outfit', sans-serif;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
}

body {
    background-color: var(--bg-color);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    color: var(--text-primary);
}

/* Background Atmosphere */
.background-globes {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
    overflow: hidden;
}

.globe {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.4;
}

.g1 {
    width: 400px;
    height: 400px;
    background: #4f46e5;
    top: -100px;
    left: -100px;
}

.g2 {
    width: 300px;
    height: 300px;
    background: #c026d3;
    bottom: -50px;
    right: -50px;
}

.g3 {
    width: 200px;
    height: 200px;
    background: #0ea5e9;
    top: 40%;
    left: 40%;
    opacity: 0.2;
}

/* Calculator Body */
.calculator-container {
    width: 360px;
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    transform: translateY(0);
    animation: floatIn 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}

@keyframes floatIn {
    from { opacity: 0; transform: translateY(40px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

/* Display */
.display-container {
    height: 140px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    padding: 0 8px 16px 8px;
    margin-bottom: 12px;
}

.history {
    font-size: 16px;
    color: var(--text-secondary);
    margin-bottom: 8px;
    height: 20px;
    opacity: 0.7;
}

.result {
    font-size: 56px;
    font-weight: 300;
    line-height: 1.1;
    letter-spacing: -1px;
    word-break: break-all;
    text-align: right;
    width: 100%;
}

/* Keypad */
.keypad {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
}

button {
    height: 70px;
    border-radius: 20px;
    border: none;
    background: var(--btn-bg);
    color: var(--text-primary);
    font-size: 24px;
    font-weight: 400;
    cursor: pointer;
    transition: all 0.15s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    outline: none;
}

button:active {
    transform: scale(0.92);
}

/* Button Variants */
.num {
    background: rgba(255,255,255,0.03);
}

.num:hover {
    background: rgba(255,255,255,0.08);
}

.func {
    color: #a3a3a3;
    font-size: 20px;
}

.func:hover {
    background: rgba(255,255,255,0.1);
    color: #fff;
}

.op {
    background: rgba(255, 159, 28, 0.15);
    color: var(--op-color);
    font-size: 28px;
}

.op:hover {
    background: rgba(255, 159, 28, 0.3);
}

.equal {
    background: var(--accent);
    color: white;
    grid-column: span 1; /* Was thinking span 2 maybe? Standard allows 1 usually */
    box-shadow: 0 0 20px var(--accent-glow);
}

.equal:hover {
    filter: brightness(1.1);
    box-shadow: 0 0 30px var(--accent-glow);
}

.zero {
    grid-column: span 2;
    padding-left: 28px;
    justify-content: flex-start;
}

/* Animation Classes */
.ripple {
    position: relative;
    overflow: hidden;
}

.ripple::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.2);
    top: 0;
    left: 0;
    opacity: 0;
    border-radius: inherit;
    animation: rip 0.3s ease-out;
}

@keyframes rip {
    0% { transform: scale(0.5); opacity: 1; }
    100% { transform: scale(1.5); opacity: 0; }
}
"""

CALCULATOR_JS = """/**
 * Quantum Calculator Logic
 * Handles arithmetic, history, and animations.
 */

class Calculator {
    constructor(historyEl, resultEl) {
        this.historyEl = historyEl;
        this.resultEl = resultEl;
        this.clear();
        this.readyToReset = false;
    }

    clear() {
        this.currentOperand = '0';
        this.previousOperand = '';
        this.operation = undefined;
        this.updateDisplay();
    }

    delete() {
        if (this.readyToReset) {
            this.clear();
            return;
        }
        if (this.currentOperand === '0') return;
        this.currentOperand = this.currentOperand.toString().slice(0, -1);
        if (this.currentOperand === '') this.currentOperand = '0';
        this.updateDisplay();
    }

    appendNumber(number) {
        if (this.readyToReset) {
            this.currentOperand = number;
            this.readyToReset = false;
            this.updateDisplay();
            return;
        }
        if (number === '.' && this.currentOperand.includes('.')) return;
        if (this.currentOperand === '0' && number !== '.') {
            this.currentOperand = number;
        } else {
            this.currentOperand = this.currentOperand.toString() + number.toString();
        }
        this.updateDisplay();
    }

    chooseOperation(operation) {
        if (this.currentOperand === '') return;
        if (this.previousOperand !== '') {
            this.compute();
        }
        this.operation = operation;
        this.previousOperand = this.currentOperand;
        this.currentOperand = '';
    }

    compute() {
        let computation;
        const prev = parseFloat(this.previousOperand);
        const current = parseFloat(this.currentOperand);
        if (isNaN(prev) || isNaN(current)) return;
        
        switch (this.operation) {
            case '+': computation = prev + current; break;
            case '-': computation = prev - current; break;
            case '*': computation = prev * current; break;
            case '/': computation = prev / current; break;
            default: return;
        }
        
        this.currentOperand = computation;
        this.operation = undefined;
        this.previousOperand = '';
        this.readyToReset = true;
        this.updateDisplay();
    }

    getDisplayNumber(number) {
        const stringNumber = number.toString();
        const integerDigits = parseFloat(stringNumber.split('.')[0]);
        const decimalDigits = stringNumber.split('.')[1];
        let integerDisplay;
        if (isNaN(integerDigits)) {
            integerDisplay = '';
        } else {
            integerDisplay = integerDigits.toLocaleString('en', { maximumFractionDigits: 0 });
        }
        if (decimalDigits != null) {
            return `${integerDisplay}.${decimalDigits}`;
        } else {
            return integerDisplay;
        }
    }

    updateDisplay() {
        this.resultEl.innerText = this.getDisplayNumber(this.currentOperand);
        if (this.operation != null) {
            this.historyEl.innerText = `${this.getDisplayNumber(this.previousOperand)} ${this.operation}`;
        } else {
            this.historyEl.innerText = '';
        }
        
        // Dynamic Font Scaling
        if (this.currentOperand.toString().length > 9) {
            this.resultEl.style.fontSize = '36px';
        } else if (this.currentOperand.toString().length > 6) {
            this.resultEl.style.fontSize = '46px';
        } else {
            this.resultEl.style.fontSize = '56px';
        }
    }

    negate() {
        if (this.currentOperand === '0') return;
        this.currentOperand = (parseFloat(this.currentOperand) * -1).toString();
        this.updateDisplay();
    }

    percent() {
        this.currentOperand = (parseFloat(this.currentOperand) / 100).toString();
        this.updateDisplay();
    }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
    const historyEl = document.getElementById('history');
    const resultEl = document.getElementById('result');
    const calculator = new Calculator(historyEl, resultEl);

    // Button Clicks
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', () => {
            // Ripple Effect
            button.classList.add('ripple');
            setTimeout(() => button.classList.remove('ripple'), 300);
            
            // Logic
            if (button.classList.contains('num')) {
                if (button.dataset.num) calculator.appendNumber(button.dataset.num);
                if (button.dataset.action === '.') calculator.appendNumber('.');
            }
            if (button.classList.contains('op')) {
                calculator.chooseOperation(button.dataset.action);
            }
            if (button.dataset.action === 'AC') calculator.clear();
            if (button.dataset.action === '=') calculator.compute();
            if (button.dataset.action === '+/-') calculator.negate();
            if (button.dataset.action === '%') calculator.percent();
        });
    });

    // Keyboard support
    document.addEventListener('keydown', (e) => {
        if ((e.key >= 0 && e.key <= 9) || e.key === '.') calculator.appendNumber(e.key);
        if (e.key === '=' || e.key === 'Enter') calculator.compute();
        if (e.key === 'Backspace') calculator.delete();
        if (e.key === 'Escape') calculator.clear();
        if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') calculator.chooseOperation(e.key);
    });
});
"""
