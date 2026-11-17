// CSS Grid Calculator - Task 3 (CodSoft Level 1)

class Calculator {
  constructor(displayMain, displayExpression, operatorIndicator) {
    this.displayMain = displayMain;
    this.displayExpression = displayExpression;
    this.operatorIndicator = operatorIndicator;
    this.history = [];
    this.soundEnabled = true;
    this.clearAll();
  }

  clearAll() {
    this.currentOperand = '0';
    this.previousOperand = '';
    this.operation = undefined;
    this.shouldResetScreen = false;
    this.updateDisplay();
  }

  deleteDigit() {
    if (this.shouldResetScreen) {
      this.currentOperand = '0';
      this.shouldResetScreen = false;
      this.updateDisplay();
      return;
    }

    if (this.currentOperand.length === 1 || (this.currentOperand.length === 2 && this.currentOperand.startsWith('-'))) {
      this.currentOperand = '0';
    } else {
      this.currentOperand = this.currentOperand.slice(0, -1);
    }
    this.updateDisplay();
  }

  appendNumber(number) {
    if (this.shouldResetScreen) {
      this.currentOperand = '';
      this.shouldResetScreen = false;
    }

    // If current is '0', replace it (unless appending dot)
    if (this.currentOperand === '0' && number !== '.') {
      this.currentOperand = number.toString();
    } else {
      this.currentOperand += number.toString();
    }
    this.updateDisplay();
  }

  appendDecimal() {
    if (this.shouldResetScreen) {
      this.currentOperand = '0';
      this.shouldResetScreen = false;
    }
    if (!this.currentOperand.includes('.')) {
      this.currentOperand += '.';
    }
    this.updateDisplay();
  }

  chooseOperation(op) {
    if (this.currentOperand === '' && this.previousOperand === '') return;

    if (this.currentOperand === '' && this.previousOperand !== '') {
      // User is changing the operator
      this.operation = op;
      this.updateDisplay();
      return;
    }

    if (this.previousOperand !== '') {
      this.compute(false);
    }

    this.operation = op;
    this.previousOperand = this.currentOperand;
    this.currentOperand = '';
    this.updateDisplay();
  }

  applyPercent() {
    const current = parseFloat(this.currentOperand);
    if (isNaN(current)) return;
    this.currentOperand = this.formatPrecision(current / 100);
    this.updateDisplay();
  }

  negate() {
    const current = parseFloat(this.currentOperand);
    if (isNaN(current) || current === 0) return;
    this.currentOperand = (-current).toString();
    this.updateDisplay();
  }

  applyFunction(func) {
    const current = parseFloat(this.currentOperand);
    if (isNaN(current)) return;

    let res = 0;
    let desc = '';

    if (func === 'sqrt') {
      if (current < 0) {
        this.currentOperand = 'Error';
        this.shouldResetScreen = true;
        this.updateDisplay();
        return;
      }
      res = Math.sqrt(current);
      desc = `√(${current})`;
    } else if (func === 'pow') {
      res = Math.pow(current, 2);
      desc = `sqr(${current})`;
    } else if (func === 'pi') {
      res = Math.PI;
      desc = 'π';
    }

    const formatted = this.formatPrecision(res);
    this.addHistory(desc, formatted);
    this.currentOperand = formatted;
    this.shouldResetScreen = true;
    this.updateDisplay();
  }

  compute(isEqualsPressed = true) {
    let computation;
    const prev = parseFloat(this.previousOperand);
    const current = parseFloat(this.currentOperand);

    if (isNaN(prev) || isNaN(current)) return;

    // Using explicit if-else statements for operations
    if (this.operation === '+') {
      computation = prev + current;
    } else if (this.operation === '-') {
      computation = prev - current;
    } else if (this.operation === '*') {
      computation = prev * current;
    } else if (this.operation === '/') {
      if (current === 0) {
        this.currentOperand = 'Cannot divide by 0';
        this.previousOperand = '';
        this.operation = undefined;
        this.shouldResetScreen = true;
        this.updateDisplay();
        return;
      }
      computation = prev / current;
    } else {
      return;
    }

    const opSymbol = this.getOperatorSymbol(this.operation);
    const expressionString = `${prev} ${opSymbol} ${current}`;
    const resultString = this.formatPrecision(computation);

    if (isEqualsPressed) {
      this.addHistory(expressionString, resultString);
      this.currentOperand = resultString;
      this.previousOperand = '';
      this.operation = undefined;
      this.shouldResetScreen = true;
    } else {
      this.currentOperand = resultString;
    }

    this.updateDisplay();
  }

  formatPrecision(num) {
    // Avoid floating point precision issues like 0.1 + 0.2 = 0.30000000000000004
    const rounded = parseFloat(num.toFixed(10));
    return rounded.toString();
  }

  getOperatorSymbol(op) {
    if (op === '+') return '+';
    if (op === '-') return '−';
    if (op === '*') return '×';
    if (op === '/') return '÷';
    return '';
  }

  addHistory(calc, result) {
    this.history.unshift({ calc, result });
    if (this.history.length > 20) this.history.pop();
    renderHistory(this.history);
  }

  updateDisplay() {
    this.displayMain.textContent = this.currentOperand || '0';
    if (this.operation != null && this.previousOperand !== '') {
      this.displayExpression.textContent = `${this.previousOperand} ${this.getOperatorSymbol(this.operation)}`;
      this.operatorIndicator.textContent = this.getOperatorSymbol(this.operation);
    } else {
      this.displayExpression.textContent = '';
      this.operatorIndicator.textContent = '';
    }

    // Dynamic font resizing for long output strings
    if (this.displayMain.textContent.length > 11) {
      this.displayMain.style.fontSize = '1.75rem';
    } else if (this.displayMain.textContent.length > 8) {
      this.displayMain.style.fontSize = '2.2rem';
    } else {
      this.displayMain.style.fontSize = '2.75rem';
    }
  }
}

// Global Audio Context Synthesizer for tactile click sound
let audioCtx = null;
function playClickSound() {
  if (!calc.soundEnabled) return;
  try {
    if (!audioCtx) {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(440, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.03);
    gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.03);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.03);
  } catch (e) {
    // Audio context may not be supported or allowed yet
  }
}

// DOM Setup & Bindings
const displayMain = document.getElementById('display-main');
const displayExpression = document.getElementById('display-expression');
const operatorIndicator = document.getElementById('current-op');
const historyList = document.getElementById('history-list');

const calc = new Calculator(displayMain, displayExpression, operatorIndicator);

// Use a loop to bind events to all buttons
const allCalcButtons = document.querySelectorAll('.calc-btn, .btn-tool');
for (let i = 0; i < allCalcButtons.length; i++) {
  const btn = allCalcButtons[i];

  btn.addEventListener('click', () => {
    playClickSound();

    if (btn.hasAttribute('data-num')) {
      calc.appendNumber(btn.getAttribute('data-num'));
    } else if (btn.hasAttribute('data-op')) {
      calc.chooseOperation(btn.getAttribute('data-op'));
    } else if (btn.hasAttribute('data-action')) {
      const action = btn.getAttribute('data-action');
      if (action === 'clear') {
        calc.clearAll();
      } else if (action === 'delete') {
        calc.deleteDigit();
      } else if (action === 'decimal') {
        calc.appendDecimal();
      } else if (action === 'percent') {
        calc.applyPercent();
      } else if (action === 'negate') {
        calc.negate();
      } else if (action === 'calculate') {
        calc.compute(true);
      } else if (action === 'sqrt' || action === 'pow' || action === 'pi') {
        calc.applyFunction(action);
      } else if (action === 'copy') {
        copyToClipboard(calc.currentOperand);
      }
    }
  });
}

// Render History
function renderHistory(historyArray) {
  if (!historyList) return;
  if (historyArray.length === 0) {
    historyList.innerHTML = `
      <div class="history-empty">
        <i class="fa-solid fa-calculator"></i>
        <p>No calculations yet.<br>Perform an operation to view history.</p>
      </div>`;
    return;
  }

  let html = '';
  for (let j = 0; j < historyArray.length; j++) {
    const item = historyArray[j];
    html += `
      <div class="history-item" data-value="${item.result}">
        <div class="history-calc">${item.calc} =</div>
        <div class="history-res">${item.result}</div>
      </div>
    `;
  }
  historyList.innerHTML = html;

  // Add click to history items to restore
  const items = historyList.querySelectorAll('.history-item');
  for (let k = 0; k < items.length; k++) {
    items[k].addEventListener('click', () => {
      const val = items[k].getAttribute('data-value');
      calc.currentOperand = val;
      calc.shouldResetScreen = true;
      calc.updateDisplay();
    });
  }
}

// Clear History Button
const clearHistoryBtn = document.getElementById('clear-history-btn');
if (clearHistoryBtn) {
  clearHistoryBtn.addEventListener('click', () => {
    calc.history = [];
    renderHistory([]);
  });
}

// Clipboard Copy
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    const toast = document.getElementById('copy-toast');
    if (toast) {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2000);
    }
  }).catch(() => {
    alert(`Current value: ${text}`);
  });
}

// Keyboard Support
window.addEventListener('keydown', (e) => {
  if (e.key >= '0' && e.key <= '9') {
    playClickSound();
    calc.appendNumber(e.key);
  } else if (e.key === '.') {
    playClickSound();
    calc.appendDecimal();
  } else if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') {
    playClickSound();
    calc.chooseOperation(e.key);
  } else if (e.key === 'Enter' || e.key === '=') {
    e.preventDefault();
    playClickSound();
    calc.compute(true);
  } else if (e.key === 'Backspace') {
    playClickSound();
    calc.deleteDigit();
  } else if (e.key === 'Escape') {
    playClickSound();
    calc.clearAll();
  } else if (e.key === '%') {
    playClickSound();
    calc.applyPercent();
  }
});

// Sound Toggle
const soundToggle = document.getElementById('sound-toggle');
if (soundToggle) {
  soundToggle.addEventListener('click', () => {
    calc.soundEnabled = !calc.soundEnabled;
    soundToggle.classList.toggle('active', calc.soundEnabled);
    const icon = soundToggle.querySelector('i');
    icon.className = calc.soundEnabled ? 'fa-solid fa-volume-high' : 'fa-solid fa-volume-xmark';
  });
}

// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    const icon = themeToggle.querySelector('i');
    icon.className = next === 'dark' ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
  });
}

// History Panel Toggle for Mobile
const historyToggle = document.getElementById('history-toggle');
const historyPanel = document.getElementById('history-panel');
if (historyToggle && historyPanel) {
  historyToggle.addEventListener('click', () => {
    historyPanel.classList.toggle('mobile-open');
    historyToggle.classList.toggle('active');
  });
}
