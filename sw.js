// Service Worker - 让网页可以像 App 一样使用
const CACHE_NAME = 'prefects-v1';

// 安装时缓存文件
self.addEventListener('install', event => {
    console.log('Service Worker 安装成功');
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll([
                '/',
                '/index.html',
                '/manifest.json'
            ]);
        })
    );
});

// 请求时优先从缓存读取
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
