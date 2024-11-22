<?php

use Illuminate\Support\Facades\Route;
use App\Events\UserRegistered;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
Route::get('/emit-event', function () {
    event(new UserRegistered('john_doe'));
    return 'Event emitted!';
});

Route::get('/', function () {
    return view('welcome');
});
