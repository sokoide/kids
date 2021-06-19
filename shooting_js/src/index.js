import "./styles.css";
import { keyboard } from "./util.js";
import * as PIXI from "pixi.js";

// PIXIの初期設定
let type = "WebGL";
if (!PIXI.utils.isWebGLSupported()) {
	type = "canvas";
}

// PIXIのテスト
PIXI.utils.sayHello(type);

// 定数
const loader = PIXI.Loader.shared;
const sprites = {};

// appの作成
let app = new PIXI.Application({
	width: 640,
	height: 480,
	backgroundColor: 0x000000
});

// appの登録
document.body.appendChild(app.view);

// spriteの読み込み
loader.add("alien1", "./images/alien1.png", { crossOrigin: "anonymous" });
loader.add("alien2", "./images/alien2.png", { crossOrigin: "anonymous" });
loader.add("alien3", "./images/alien3.png", { crossOrigin: "anonymous" });
loader.add("player", "./images/player.png", { crossOrigin: "anonymous" });
loader.add("missile", "./images/missile.png", { crossOrigin: "anonymous" });
loader.add("alien_missile", "./images/alien_missile.png", {
	crossOrigin: "anonymous"
});
loader.add("laser", "./images/laser.png", { crossOrigin: "anonymous" });
loader.load((loader, resources) => {
	sprites.player = new PIXI.Sprite(resources.player.texture);
	sprites.player.anchor.set(0.5);
	sprites.player.x = 320;
	sprites.player.y = 440;
	sprites.player.vx = 0;
	app.stage.addChild(sprites.player);

	setup();

	//　スケジューラーの登録
	// app.ticker.add内のfunctionは1秒間に60回呼ばれます
	app.ticker.add(function (delta) {
		gameloop(delta);
	});
});

function setup() {
	let left = keyboard("ArrowLeft"),
		right = keyboard("ArrowRight"),
		space = keyboard(" ");

	left.press = () => {
		sprites.player.vx = -4;
	};
	right.press = () => {
		sprites.player.vx = 4;
	};
	space.press = () => {
		console.info("fire!");
	};
	left.release = () => {
		if (sprites.player.vx === -4) {
			sprites.player.vx = 0;
		}
	};
	right.release = () => {
		if (sprites.player.vx === 4) {
			sprites.player.vx = 0;
		}
	};
}

// ここで各種チェック、処理を行います
function gameloop(delta) {
	sprites.player.x += sprites.player.vx;
}

