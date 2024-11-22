<?php

namespace App\Listeners;

use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Queue\InteractsWithQueue;

class SendWelcomeEmail {
    public function handle(UserRegistered $event) {
        echo "Sending welcome email to " . $event->username;
        }
       }
       
   