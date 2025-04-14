local wezterm = require 'wezterm'
local config = wezterm.config_builder()

-- Color Scheme
config.color_scheme = "catppuccin-mocha"
config.colors = {
    tab_bar = {
        background = '#313244',
        active_tab = {
           bg_color = '#11111b',
           fg_color = '#cdd6f4',
           underline = 'Single'
        },
        inactive_tab = {
            bg_color = '#313244',
            fg_color = '#a6adc8'
        },
        inactive_tab_hover = {
            bg_color = '#585b70',
            fg_color = '#bac2de',
            italic = true;
        },
        new_tab = {
            bg_color = '#313244',
            fg_color = '#bac2de',
        },
        new_tab_hover = {
            bg_color = '#585b70',
            fg_color = '#bac2de',
            italic = true,
        },
    }
}

-- Tab Settings
config.use_fancy_tab_bar = false
config.tab_bar_at_bottom = true

-- Update Settings
config.check_for_updates = false

-- Inactive Tab Settings
config.inactive_pane_hsb = {
    saturation = 0.9,
    brightness = 0.6,
}

-- Window Opacity
config.window_background_opacity = 0.95

-- Font Settings
config.font = wezterm.font 'JetBrains Mono'

-- Keybindings
local action = wezterm.action
config.keys = {
    {
        key = 'o',
        mods = 'CTRL|SHIFT',
        action = action.SplitHorizontal { domain = 'CurrentPaneDomain' },
    },
    {
        key = 'e',
        mods = 'CTRL|SHIFT',
        action = action.SplitVertical { domain = 'CurrentPaneDomain' },
    },
    { 
        key = 'l', 
        mods = 'ALT', 
        action = action.ShowLauncher, 
    },
    {
        key = 'LeftArrow',
        mods = 'CTRL|ALT',
        action = action.ActivateTabRelative(-1),
    },
    {
        key = 'RightArrow',
        mods = "CTRL|ALT",
        action = action.ActivateTabRelative(1),
    },
    {
        key = 'w',
        mods = "CTRL|ALT|SHIFT",
        action = wezterm.action.AttachDomain 'unix-ssh01',
    },
}

-- Domain Config
config.ssh_domains = {
    {
        name = 'vm',
        remote_address = 'vm',
        local_echo_threshold_ms = 10,
    },
}
config.unix_domains = {
    {
        name = 'unix-ssh01',
        proxy_command = {
            "ssh",
            "-T",
            "ssh01",
            "wezterm",
            "cli",
            "proxy"
        },
        local_echo_threshold_ms = 10,
    },
}

-- Show latency in the status area
wezterm.on('update-right-status', function(window, pane)
  local meta = pane:get_metadata() or {}
  if meta.is_tardy then
    local secs = meta.since_last_response_ms / 1000.0
    window:set_right_status(string.format('tardy: %5.1fs⏳', secs))
  end
end)

return config

