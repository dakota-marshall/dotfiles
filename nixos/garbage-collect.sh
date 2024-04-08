#!/usr/bin/env bash

# Deletes all generations, but keeps the 3 latest, for rollback purposes
sudo nix-collect-garbage --delete-older-than +3
