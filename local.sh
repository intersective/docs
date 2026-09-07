#!/bin/bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PORT=8000
DEV_ADDR="127.0.0.1:${PORT}"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}🚀 Starting Local Development Server${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Change to project directory
cd "$PROJECT_DIR"

# Function to check if port is in use
check_port() {
    if lsof -ti:${PORT} > /dev/null 2>&1; then
        return 0  # Port is in use
    else
        return 1  # Port is free
    fi
}

# Function to kill existing server
cleanup_server() {
    if check_port; then
        echo -e "${YELLOW}⚠️  Found existing server(s) on port ${PORT}${NC}"
        
        # Get ALL PIDs using the port (handles multiple processes)
        PIDS=$(lsof -ti:${PORT} 2>/dev/null || true)
        
        if [ -z "$PIDS" ]; then
            echo -e "${GREEN}✅ Port ${PORT} is now available${NC}"
            return 0
        fi
        
        echo -e "${YELLOW}🛑 Stopping processes (PIDs: ${PIDS})...${NC}"
        
        # Kill all processes gracefully first
        for PID in $PIDS; do
            kill ${PID} 2>/dev/null || true
        done
        
        # Wait a bit for graceful shutdown
        sleep 3
        
        # Check if any processes are still running and force kill them
        REMAINING_PIDS=$(lsof -ti:${PORT} 2>/dev/null || true)
        if [ -n "$REMAINING_PIDS" ]; then
            echo -e "${YELLOW}⚠️  Force killing remaining processes...${NC}"
            for PID in $REMAINING_PIDS; do
                kill -9 ${PID} 2>/dev/null || true
            done
            sleep 2
        fi
        
        # Final check
        if ! check_port; then
            echo -e "${GREEN}✅ All processes stopped successfully${NC}"
        else
            # Last resort: try to kill all remaining processes
            FINAL_PIDS=$(lsof -ti:${PORT} 2>/dev/null || true)
            if [ -n "$FINAL_PIDS" ]; then
                echo -e "${YELLOW}⚠️  Attempting final cleanup...${NC}"
                for PID in $FINAL_PIDS; do
                    kill -9 ${PID} 2>/dev/null || true
                done
                sleep 1
                
                if ! check_port; then
                    echo -e "${GREEN}✅ Port ${PORT} is now free${NC}"
                else
                    echo -e "${RED}❌ Failed to free port ${PORT}. Please check manually:${NC}"
                    echo -e "${RED}   Run: lsof -ti:${PORT} | xargs kill -9${NC}"
                    exit 1
                fi
            else
                echo -e "${GREEN}✅ Port ${PORT} is now free${NC}"
            fi
        fi
    else
        echo -e "${GREEN}✅ Port ${PORT} is available${NC}"
    fi
}

# Function to validate dependencies
check_dependencies() {
    echo -e "\n${BLUE}🔍 Checking dependencies...${NC}"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python 3 is not installed${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Python 3 found${NC}"
    
    # Check MkDocs
    if ! command -v mkdocs &> /dev/null; then
        echo -e "${YELLOW}⚠️  MkDocs not found. Installing dependencies...${NC}"
        pip3 install -q -r requirements.txt
    else
        echo -e "${GREEN}✅ MkDocs found${NC}"
    fi
    
    # Validate MkDocs config
    if python3 scripts/validate_mkdocs.py > /dev/null 2>&1; then
        echo -e "${GREEN}✅ MkDocs configuration valid${NC}"
    else
        echo -e "${YELLOW}⚠️  MkDocs configuration validation had warnings${NC}"
    fi
}

# Function to build site
build_site() {
    echo -e "\n${BLUE}🔨 Building site (clean build)...${NC}"
    if mkdocs build --clean > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Site built successfully${NC}"
    else
        echo -e "${YELLOW}⚠️  Build had warnings (continuing anyway)${NC}"
    fi
}

# Function to start server
start_server() {
    echo -e "\n${BLUE}🚀 Starting MkDocs development server...${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}📍 Local URL: http://${DEV_ADDR}${NC}"
    echo -e "${GREEN}📍 Alternative: http://localhost:${PORT}${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}💡 Press Ctrl+C to stop the server${NC}\n"
    
    # Start MkDocs server
    mkdocs serve --dev-addr="${DEV_ADDR}"
}

# Main execution
main() {
    # Cleanup existing server
    cleanup_server
    
    # Check dependencies
    check_dependencies
    
    # Build site to ensure fresh content
    build_site
    
    # Start server
    start_server
}

# Handle script interruption
trap 'echo -e "\n${YELLOW}🛑 Server stopped by user${NC}"; exit 0' INT TERM

# Run main function
main
