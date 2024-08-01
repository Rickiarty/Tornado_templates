const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    },
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 }, // 移除重力效果
            debug: false
        }
    }
};

const game = new Phaser.Game(config);
const MAX_BALLS = 2000; // 設定臨界值(最大容忍值)
let lastUpdateTime = 0; // 上次更新的時間

function preload() {
    this.load.image('ball', 'image/microbe01.png'); // 使用相對路徑
    this.load.image('background', 'image/background.png'); // 載入背景圖片
    this.load.audio('gameOverSound', 'audio/gameOverSound.mp3'); // 載入哀號聲
}

function create() {
    this.add.image(400, 300, 'background'); // 設置背景圖片

    this.balls = this.physics.add.group();
    this.balls.create(400, 300, 'ball').setScale(0.5); // 初始球體在視野中央

    this.ballCountText = this.add.text(650, 550, 'Balls: 1', { fontSize: '20px', fill: '#000' }); // 顯示球體數量

    const splitBalls = () => {
        const newBalls = [];
        this.balls.children.iterate((ball) => {
            const x = ball.x;
            const y = ball.y;
            newBalls.push(this.balls.create(x + Phaser.Math.Between(-10, 10), y + Phaser.Math.Between(-10, 10), 'ball').setScale(0.5));
            newBalls.push(this.balls.create(x + Phaser.Math.Between(-10, 10), y + Phaser.Math.Between(-10, 10), 'ball').setScale(0.5));
            ball.destroy(); // 移除原始球體
        });

        this.ballCountText.setText('Balls: ' + this.balls.getChildren().length);

        if (this.balls.getChildren().length > MAX_BALLS) {
            this.sound.play('gameOverSound'); // 播放哀號聲
            this.add.text(300, 250, 'GAME OVER', { fontSize: '64px', fill: '#f00' });
            this.scene.pause(); // 暫停遊戲
        }
    };

    this.input.keyboard.on('keydown-SPACE', splitBalls);
    this.input.on('pointerdown', splitBalls); // 添加點擊螢幕事件
}

function update(time) {
    if (time - lastUpdateTime > 100) { // 每 0.1 秒更新一次
        lastUpdateTime = time;

        Phaser.Actions.Call(this.balls.getChildren(), function(ball) {
            ball.x += Phaser.Math.Between(-269, 269);
            ball.y += Phaser.Math.Between(-269, 269);

            // 確保球體不會移出螢幕
            if (ball.x < 0) ball.x = 0;
            if (ball.x > 800) ball.x = 800;
            if (ball.y < 0) ball.y = 0;
            if (ball.y > 600) ball.y = 600;
        }, this);
    }
}
