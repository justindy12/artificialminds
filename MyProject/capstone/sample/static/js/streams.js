const APP_ID ='159e408dc336412c866e33b34ba9d40b'
const TOKEN = '3bd84fa19e49422b9fd4464da986866a'
let UID;
console.log('Stream.js connected')

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
	UID = await client.join(APP_ID, TOKEN, null)

	localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

	let player ='<div class="video-container" id="user-container-${UID}"><div class="username-wrapper"><span class="user-name">My Name</span></div><div class="video-player" id="user-${UID}"></div></div>'

	document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

	localTracks[1].play('user-${UID}')

	await client.publish([localTracks[0]. localTracks[1]])
}

joinAndDisplayLocalStream()